#MenuTitle: Make component glyph for all masters
# -*- coding: utf-8 -*-
# by Pedro Arilla
__doc__="""
Builds compound glyphs in the selected ones for all masters.
"""

import GlyphsApp
import time
Glyphs.clearLog()
print "Make component glyph for all masters @ " + time.strftime("%H:%M:%S")

thisFont = Glyphs.font
listOfSelectedLayers = thisFont.selectedLayers
for selectedLayer in listOfSelectedLayers:
    thisGlyph = selectedLayer.parent
    for layer in thisGlyph.layers:
        layer.makeComponents()

print "Compound glyphs built."
