#MenuTitle: abcdefghijk...
# -*- coding: utf-8 -*-
# by Pedro Arilla
from __future__ import division, print_function, unicode_literals
__doc__="""
Opens a new tab and outputs selected glyph(s) between lowercase a-z.
"""

import GlyphsApp, time, random
Glyphs.clearLog()
print("New tab with glyp(s) between lowercase @ " + time.strftime("%H:%M:%S"))

thisFont = Glyphs.font
selectedLayers = thisFont.selectedLayers
abecedary = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
tabString = ""

for n in selectedLayers:
	for i in abecedary:
		tabString += "/" + n.parent.name
		tabString += "/" + i
	tabString += "/" + n.parent.name + '\n\n'

thisFont.newTab(tabString)

print("Tab with glyph(s) between lowercase opened.")
