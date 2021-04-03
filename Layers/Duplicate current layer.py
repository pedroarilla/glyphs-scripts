#MenuTitle: Duplicate current layer
# -*- coding: utf-8 -*-
# by Pedro Arilla
from __future__ import division, print_function, unicode_literals
__doc__="""
Duplicates the current layer as a normal glyph layer.
"""

import GlyphsApp, time
Glyphs.clearLog()
print("Duplicate current layer @ " + time.strftime("%H:%M:%S"))

thisFont = Glyphs.font
currentLayer = thisFont.selectedLayers[0]
currentGlyph = currentLayer.parent
newLayer = currentLayer.copy()
newLayer.name = '@ '+ time.strftime("%H:%M, %d/%m/%y")
thisFont.glyphs[currentGlyph.name].layers.append(newLayer)

print("Layer duplicated.")
