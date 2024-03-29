#MenuTitle: lowercase non-text
# -*- coding: utf-8 -*-
# by Pedro Arilla
from __future__ import division, print_function, unicode_literals
__doc__="""
Opens a new tab and outputs random lowercase non-text.
"""

import GlyphsApp, time, random
Glyphs.clearLog()
print("New tab with random lowercase non-text @ " + time.strftime("%H:%M:%S"))

abecedary = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
divisors = [3, 5, 7]
words = ""

for i in range(700):
    words = words + random.choice(abecedary)
    if i % random.choice(divisors) == 0:
        words = words + " "
Font.newTab(words)

print("Tab with random lowercase non-text opened.")
