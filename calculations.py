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
import math
import person

def get_random_percent (digits_after_coma):
    if digits_after_coma == 0:
        r = random.randint (0, 99)
    elif digits_after_coma > 0:
        r = random.randint (0, 99*10**digits_after_coma)/(10**digits_after_coma)
    return r

def get_random_int (min_i, max_i):
    return random.randint (min_i, max_i)

def calculate_distance (p1, p2):
    (x1, y1) = p1.get_positition ()
    (x2, y2) = p2.get_positition ()
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def propagate_health_state (p1, p2):
    if p1.can_infect() and not p2.is_immune ():
        p2.infect ()
