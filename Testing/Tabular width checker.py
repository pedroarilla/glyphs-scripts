#MenuTitle: Tabular width checker
# -*- coding: utf-8 -*-
# by Pedro Arilla
from __future__ import division, print_function, unicode_literals
__doc__="""
Checks all selected Glyphs are on same width. It ignores ‘Auto’ and makes sure that the assigned value is equal regardless of metrics keys.

Note: The glyph selected firstly sets the *master width*.
"""

import GlyphsApp, time
Glyphs.clearLog()
Glyphs.showMacroWindow()
print("Tabular width checker @ " + time.strftime("%H:%M:%S"))

thisFont = Glyphs.font
selectedLayers = thisFont.selectedLayers
masterWidth = selectedLayers[0].width
sameWidthCounter = 0
differentWidthCounter = 0
for layer in selectedLayers:
	width = layer.width
	if width == masterWidth:
		print("\t✅ " + layer.parent.name + " (%i)" % width)
		sameWidthCounter += 1
	else:
		print("\t❌ " + layer.parent.name + " (%i)" % width)
		differentWidthCounter += 1
print("Result:")
print("%i glyphs are on same width." % sameWidthCounter)
print("%i glyphs are on different width." % differentWidthCounter)
