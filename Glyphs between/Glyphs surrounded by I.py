#MenuTitle: I_I
# -*- coding: utf-8 -*-
# by Pedro Arilla
from __future__ import division, print_function, unicode_literals
__doc__="""
Opens a new tab and outputs selected glyph(s) surrounded by I string.
"""

import GlyphsApp, time, random
Glyphs.clearLog()
print("New tab with glyp(s) surrounded by I @ " + time.strftime("%H:%M:%S"))

thisFont = Glyphs.font
selectedLayers = thisFont.selectedLayers
testString = "/I"
tabString = ""

for n in selectedLayers:
	tabString += testString
	tabString += "/" + n.parent.name
tabString += testString

thisFont.newTab(tabString)

print("Tab with glyph(s) surrounded by I opened.")
