#MenuTitle: nnonn
# -*- coding: utf-8 -*-
# by Pedro Arilla
from __future__ import division, print_function, unicode_literals
__doc__="""
Opens a new tab and outputs selected glyph(s) surrounded by nnonn string.
"""

import GlyphsApp, time, random
Glyphs.clearLog()
print("New tab with glyp(s) surrounded by nnonn @ " + time.strftime("%H:%M:%S"))

thisFont = Glyphs.font
selectedLayers = thisFont.selectedLayers
testString = "/n/n/o/n/n"
tabString = ""

for n in selectedLayers:
	tabString += testString
	tabString += "/" + n.parent.name
tabString += testString

thisFont.newTab(tabString)

print("Tab with glyph(s) surrounded by nnonn opened.")
