#MenuTitle: New tab with glyphs between figures
# -*- coding: utf-8 -*-
# by Pedro Arilla
__doc__="""
Opens a new tab and outputs selected glyph(s) between figures 0–9.
"""

import GlyphsApp
import time
import random
Glyphs.clearLog()
print "New tab with glyp(s) between figures @ " + time.strftime("%H:%M:%S")

thisFont = Glyphs.font
selectedLayers = thisFont.selectedLayers
abecedary = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tabString = ""

for n in selectedLayers:
	for i in abecedary:
		tabString += "/" + n.parent.name
		tabString += "/" + i
	tabString += "/" + n.parent.name + '\n\n'

thisFont.newTab(tabString)

print "Tab with glyph(s) between figures opened."
