#MenuTitle: New tab with glyphs between UC
# -*- coding: utf-8 -*-
# by Pedro Arilla
__doc__="""
Opens a new tab and outputs selected glyph(s) between uppercase A-Z.
"""

import GlyphsApp
import time
import random
Glyphs.clearLog()
print "New tab with glyp(s) between UC @ " + time.strftime("%H:%M:%S")

thisFont = Glyphs.font
selectedLayers = thisFont.selectedLayers
abecedary = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
tabString = ""

for n in selectedLayers:
	for i in abecedary:
		tabString += "/" + n.parent.name
		tabString += "/" + i
	tabString += "/" + n.parent.name + '\n\n'

thisFont.newTab(tabString)

print "Tab with glyph(s) between UC opened."
