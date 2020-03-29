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

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

#############################################################
# Class
#############################################################

class Graphs:

    def plot_scatter_from_lists (self, sick_x, sick_y, healthy_x, healthy_y, file_output):

        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        ax.scatter(sick_x, sick_y, color='r')
        ax.scatter(healthy_x, healthy_y, color='g')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Sick and healthy (red=sick, green=healthy)')
        plt.savefig(file_output)
        plt.close(fig)

    def plot_stackplot_from_lists (self, time, can_be_sick, sick, immune, file_output):

        y = np.vstack([can_be_sick, immune, sick])

        labels = ["can be sick ", "immune", "sick"]

        fig, ax = plt.subplots()
        
        ax.stackplot(time, can_be_sick, immune, sick, labels=labels)
        ax.legend(loc='upper left', prop={'size': 6})
        title = "healthy but can be sick:" + str(can_be_sick[-1]) + " immune:" + str(immune[-1]) + " sick:" + str(sick[-1])
        plt.title(title)
        plt.savefig(file_output)
        plt.close(fig)

    def plot_plot_from_lists (self, time, sick_avg, cured_avg, healthy_but_can_be_sick_avg, file_output):

        fig = plt.figure()
        plt.plot(time, sick_avg, 'r-', ms=1, label='Sick avg')
        plt.plot(time, cured_avg, 'g-', ms=1, label='Cured avg')
        plt.plot(time, healthy_but_can_be_sick_avg, 'b-', ms=1, label='Can be sick avg')
        red_patch = mpatches.Patch(color='red', label='Sick avg')
        green_patch = mpatches.Patch(color='green', label='Cured avg')
        blue_patch = mpatches.Patch(color='blue', label='Can be sick avg')
        plt.legend(handles=[red_patch, blue_patch, green_patch], loc='upper left', prop={'size': 6})
        plt.xlabel('Time')
        plt.ylabel('Values')
        plt.title('Average age')
        plt.grid(True)
        plt.savefig(file_output)
        plt.close(fig)
