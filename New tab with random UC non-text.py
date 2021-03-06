#MenuTitle: New tab with random UC non-text
# -*- coding: utf-8 -*-
# by Pedro Arilla
__doc__="""
Opens a new tab and outputs random uppercase non-text.
"""

import GlyphsApp
import time
import random
Glyphs.clearLog()
print "New tab with random UC non-text @ " + time.strftime("%H:%M:%S")

abecedary = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
divisors = [3, 5, 7]
words = ""

for i in range(700):
    words = words + random.choice(abecedary)
    if i % random.choice(divisors) == 0:
        words = words + " "
words = words.upper()
Font.newTab(words)

print "Tab with random UC non-text opened."
