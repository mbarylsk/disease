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
        ax.scatter(healthy_x, healthy_y, color='b')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Sick and healthy')
        plt.savefig(file_output)
        plt.close(fig)

    def plot_stackplot_from_lists (self, time, can_be_sick, sick, immune, file_output):

        y = np.vstack([can_be_sick, immune, sick])

        labels = ["can be sick ", "immune", "sick"]

        fig, ax = plt.subplots()
        
        ax.stackplot(time, can_be_sick, immune, sick, labels=labels)
        ax.legend(loc='upper left')
        title = "healthy but can be sick:" + str(can_be_sick[-1]) + " immune:" + str(immune[-1]) + " sick:" + str(sick[-1])
        plt.title(title)
        plt.savefig(file_output)
        plt.close(fig)
