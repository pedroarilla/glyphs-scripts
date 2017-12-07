#MenuTitle: Duplicate current layer
# -*- coding: utf-8 -*-
# by Pedro Arilla
__doc__="""
Duplicates the current layer as a normal glyph layer
"""

import GlyphsApp
import time

thisFont = Glyphs.font
currentLayer = thisFont.selectedLayers[0]
currentGlyph = currentLayer.parent
newLayer = currentLayer.copy()
newLayer.name = '@ '+ time.strftime("%H:%M, %d/%m/%y")
thisFont.glyphs[currentGlyph.name].layers.append(newLayer)

Glyphs.clearLog()
print "Layer duplicated."