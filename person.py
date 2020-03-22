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
    cured = False
    x = 0
    y = 0
    age = 0
    max_x = 0
    max_y = 0
    
    def __init__(self, idp, s, c, x, y, max_x, max_y):
        self.idp = idp
        self.sick = s
        self.cured = c
        self.x = x
        self.y = y
        self.max_x = max_x
        self.max_y = max_y
        self.age = 0

    def get_positition (self):
        return (self.x, self.y)

    def move (self):
        dx = random.randint (-5, 5)
        dy = random.randint (-5, 5)
        self.x = (self.x + dx) % self.max_x
        self.y = (self.y + dy) % self.max_y
        self.age += 1

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
