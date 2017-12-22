#MenuTitle: Tabular width checker
# -*- coding: utf-8 -*-
# by Pedro Arilla
__doc__="""
Checks all selected Glyphs are on same width. It ignores ‘Auto’ and makes sure that the assigned value is equal regardless of metrics keys.

Note: The glyph selected firstly sets the *master width*.
"""

import GlyphsApp
thisFont = Glyphs.font
selectedLayers = thisFont.selectedLayers
masterWidth = selectedLayers[0].width
sameWidthCounter = 0
differentWidthCounter = 0

Glyphs.clearLog()
Glyphs.showMacroWindow()
print "Processing..."

for thisLayer in selectedLayers:
	width = thisLayer.width
	if width == masterWidth:
		print "+++" + thisLayer.parent.name + ": Yep! (%i)" % width
		sameWidthCounter += 1
	else:
		print "---" + thisLayer.parent.name + ": Nope! (%i)" % width
		differentWidthCounter += 1

print "Result:"
print "%i glyphs are on same width." % sameWidthCounter
print "%i glyphs are on different width." % differentWidthCounter
