#MenuTitle: Delete all annotations
# -*- coding: utf-8 -*-
# by Pedro Arilla
__doc__="""
Delete all annotations on all layers
"""

import GlyphsApp
thisFont = Glyphs.font
noteCounter = 0

for glyph in thisFont.glyphs:
    for layer in glyph.layers:
        for annotation in layer.annotations:
            del(layer.annotations[0])
            noteCounter += 1

Glyphs.clearLog()
print "%i annotations deleted." % noteCounter
