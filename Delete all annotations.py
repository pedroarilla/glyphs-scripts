#MenuTitle: Delete all annotations
# -*- coding: utf-8 -*-
# by Pedro Arilla
__doc__="""
Deletes all annotations in all layers (masters and copies) in all glyphs.
"""

import GlyphsApp
thisFont = Glyphs.font
annotationCounter = 0

for glyph in thisFont.glyphs:
    for layer in glyph.layers:
        for annotation in layer.annotations:
            del(layer.annotations[0])
            annotationCounter += 1

Glyphs.clearLog()
Glyphs.showMacroWindow()
print "%i annotations deleted." % annotationCounter
