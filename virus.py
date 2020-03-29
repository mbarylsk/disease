# MIT License

# Copyright (c) 2020 Marcin Barylski

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import graphs
import person
import calculations
import sys

# params: max_x, max_y, max_people, min_infect_distance, cure_chance_perc, move_chance_perc, can_be_sick_again_chance_perc, no_of_turns

min_x = 0
max_x = int(sys.argv[1])
min_y = 0
max_y = int(sys.argv[2])
max_people = int(sys.argv[3])
people = []
initial_no_of_sick = 1

min_infect_distance = int(sys.argv[4])
cure_chance_perc = int(sys.argv[5])
move_chance_perc = int(sys.argv[6])
can_be_sick_again_chance_perc = int(sys.argv[7])
no_of_turns = int(sys.argv[8])
            
list_time_elapsed = []
list_can_be_sick = []
list_sick = []
list_immune = []
list_sick_time_avg = []
list_cured_time_avg = []
list_healthy_but_can_be_sick_time_avg = []

prefix = str(max_x) + "_" + str(max_y) + "_" + str(max_people) + "_" + str(min_infect_distance) + "_" + str(cure_chance_perc) + "_" + str(move_chance_perc) + "_" + str(can_be_sick_again_chance_perc) + "_" + str(no_of_turns)

file_output_trend = "results/f_" + prefix + "_trend.png"
file_output_location = "results/f_" + prefix + "_location.png"
file_output_avg = "results/f_" + prefix + "_avg.png"

def calculate_stats (time):
    global list_sick, list_can_be_sick, list_immune
    
    count_sick = 0
    count_healthy_but_can_be_sick = 0
    count_cured = 0
    total_sick_time = 0
    total_cured_time = 0
    total_healthy_but_can_be_sick_time = 0
    
    for j in range (0, max_people):
        (age_sick, age_cured, age_healthy_but_can_be_sick) = people[j].get_age()
        if people[j].is_sick():
            count_sick += 1
            total_sick_time += age_sick
        elif people[j].is_cured():
            count_cured += 1
            total_cured_time += age_cured
        else:
            count_healthy_but_can_be_sick += 1
            total_healthy_but_can_be_sick_time += age_healthy_but_can_be_sick

    list_sick.append (count_sick)
    list_can_be_sick.append (count_healthy_but_can_be_sick)
    list_immune.append (count_cured)
    list_time_elapsed.append (time)

    if count_sick > 0:
        sick_time_avg = total_sick_time/count_sick
    else:
        sick_time_avg = 0
    if count_cured > 0:
        cured_time_avg = total_cured_time/count_cured
    else:
        cured_time_avg = 0
    if count_healthy_but_can_be_sick > 0:
        healthy_but_can_be_sick_time_avg = total_healthy_but_can_be_sick_time/count_healthy_but_can_be_sick
    else:
        healthy_but_can_be_sick_time_avg = 0
        
    list_sick_time_avg.append (sick_time_avg)
    list_cured_time_avg.append (cured_time_avg)
    list_healthy_but_can_be_sick_time_avg.append (healthy_but_can_be_sick_time_avg)
    
    return (count_sick, count_healthy_but_can_be_sick, count_cured)

def print_stats (g):
    
    print ("Sick                    : ", list_sick[-1])
    print ("Healthy but can be sick : ", list_can_be_sick[-1])
    print ("Cured                   : ", list_immune[-1])

    healthy_x = []
    healthy_y = []
    sick_x = []
    sick_y = []

    for j in range (0, max_people):
        (x, y) = people[j].get_positition ()
        if people[j].is_sick():
            sick_x.append (x)
            sick_y.append (y)
        else:
            healthy_x.append (x)
            healthy_y.append (y)

    g.plot_scatter_from_lists (sick_x, sick_y, healthy_x, healthy_y, file_output_location)
    g.plot_stackplot_from_lists (list_time_elapsed, list_can_be_sick, list_sick, list_immune, file_output_trend)
    g.plot_plot_from_lists (list_time_elapsed, list_sick_time_avg, list_cured_time_avg, list_healthy_but_can_be_sick_time_avg, file_output_avg)

g = graphs.Graphs()


# set sick person
for i in range (0, max_people):
    x = calculations.get_random_int (min_x, max_x)
    y = calculations.get_random_int (min_y, max_y)
    if i < initial_no_of_sick:
        p = person.Person(i, True, True, x, y, max_x, max_y)
    else:
        p = person.Person(i, False, False, x, y, max_x, max_y)    
    people.append (p)

# main loop
for i in range (0, no_of_turns):

    calculate_stats (i)
    print_stats (g)

    # move people
    for j in range (0, max_people):
        r = calculations.get_random_percent (0)
        if r <= move_chance_perc:
            people[j].move ()

    # infect
    for j in range (0, max_people):
        for k in range (0, max_people):
            if j != k and people[j].is_sick() and calculations.calculate_distance (people[j], people[k]) < min_infect_distance and not people[k].is_cured():
                people[k].infect()

    # cure
    for j in range (0, max_people):
        if people[j].is_sick():
            r = calculations.get_random_percent (2)
            if r <= cure_chance_perc:
                people[j].cure()

    # can be sick again
    for j in range (0, max_people):
        if people[j].is_cured():
            r = calculations.get_random_percent (2)
            if r <= can_be_sick_again_chance_perc:
                people[j].healthy_but_can_be_sick_again()

    # grow
    for j in range (0, max_people):
        people[j].grow()

calculate_stats (i)
print_stats (g)
