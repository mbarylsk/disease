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

import random

#############################################################
# Class
#############################################################

class Person:
    idp = 0
    sick = False
    cured = False       # if is not seek and cured, then is immune
    x = 0
    y = 0
    age = 0
    age_sick = 0
    age_cured = 0
    age_healthy_but_can_be_sick = 0
    max_x = 0
    max_y = 0
    delta_x = 10
    delta_y = 10
    
    def __init__(self, idp, s, c, x, y, max_x, max_y):
        self.idp = idp
        self.sick = s
        self.cured = c
        self.x = x
        self.y = y
        self.max_x = max_x
        self.max_y = max_y
        self.age_sick = 0
        self.age_cured = 0

    def get_positition (self):
        return (self.x, self.y)

    def get_age (self):
        return (self.age_sick, self.age_cured, self.age_healthy_but_can_be_sick)

    def move (self):
        dx = random.randint (-self.delta_x, self.delta_x)
        dy = random.randint (-self.delta_y, self.delta_y)
        self.x = (self.x + dx) % self.max_x
        self.y = (self.y + dy) % self.max_y

    def grow (self):
        self.age += 1
        if self.is_sick():
            self.age_sick += 1
            self.age_cured = 0
            self.age_healthy_but_can_be_sick = 0
        elif self.is_cured():
            self.age_sick = 0
            self.age_cured += 1
            self.age_healthy_but_can_be_sick = 0
        else:
            self.age_sick = 0
            self.age_cured = 0
            self.age_healthy_but_can_be_sick += 1

    def set_health (self, s, c):
        self.sick = s
        self.cured = c

    def cure (self):
        self.set_health (False, True)

    def infect (self):
        self.set_health (True, False)

    def healthy_but_can_be_sick_again (self):
        self.set_health (False, False)

    def is_sick (self):
        return self.sick

    def is_cured (self):
        return self.cured
