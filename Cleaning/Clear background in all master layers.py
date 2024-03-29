#MenuTitle: Clear background in all master layers
# -*- coding: utf-8 -*-
# by Pedro Arilla
from __future__ import division, print_function, unicode_literals
__doc__="""
Clears the background in all master layers in all glyphs.
"""

import GlyphsApp, time
Glyphs.clearLog()
print("Clear background in all masters @ " + time.strftime("%H:%M:%S"))

thisFont = Glyphs.font
thisFont.disableUpdateInterface()
for glyph in thisFont.glyphs:
    for layer in glyph.layers:
        if layer.layerId == layer.associatedMasterId:
            layer.setBackground_( None )
thisFont.enableUpdateInterface()

print("All master backgrounds cleared.")
