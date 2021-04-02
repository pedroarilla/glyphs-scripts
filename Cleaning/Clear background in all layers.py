#MenuTitle: Clear background in all layers
# -*- coding: utf-8 -*-
# by Pedro Arilla
from __future__ import division, print_function, unicode_literals
__doc__="""
Clears the background in all layers (masters and copies) in all glyphs.
"""

import GlyphsApp, time
Glyphs.clearLog()
print("Clear background in all layers @ " + time.strftime("%H:%M:%S"))

thisFont = Glyphs.font
thisFont.disableUpdateInterface()
for glyph in thisFont.glyphs:
    for layer in glyph.layers:
        layer.setBackground_( None )
thisFont.enableUpdateInterface()

print("All backgrounds cleared.")
