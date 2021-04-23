#MenuTitle: 1234 56 789
# -*- coding: utf-8 -*-
# by Pedro Arilla
from __future__ import division, print_function, unicode_literals
__doc__="""
Opens a new tab and outputs random numbers.
"""

import GlyphsApp, time, random
Glyphs.clearLog()
print("New tab with random numbers @ " + time.strftime("%H:%M:%S"))

abecedary = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
divisors = [2, 3]
numbers = ""

for i in range(200):
    numbers = numbers + random.choice(abecedary)
    if i % random.choice(divisors) == 0:
        numbers = numbers + " "
Font.newTab(numbers)

print("Tab with random numbers opened.")
