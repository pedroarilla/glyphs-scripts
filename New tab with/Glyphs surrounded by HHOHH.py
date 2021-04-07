#MenuTitle: Glyphs surrounded by HHOHH
# -*- coding: utf-8 -*-
# by Pedro Arilla
from __future__ import division, print_function, unicode_literals
__doc__="""
Opens a new tab and outputs selected glyph(s) surrounded by HHOHH string.
"""

import GlyphsApp, time, random
Glyphs.clearLog()
print("New tab with glyp(s) surrounded by HHOHH @ " + time.strftime("%H:%M:%S"))

thisFont = Glyphs.font
selectedLayers = thisFont.selectedLayers
testString = "/H/H/O/H/H"
tabString = ""

for n in selectedLayers:
	tabString += testString
	tabString += "/" + n.parent.name
tabString += testString

thisFont.newTab(tabString)

print("Tab with glyph(s) surrounded by HHOHH opened.")
