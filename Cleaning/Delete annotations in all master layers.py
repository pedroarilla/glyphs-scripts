#MenuTitle: Delete annotations in all master layers
# -*- coding: utf-8 -*-
# by Pedro Arilla
from __future__ import division, print_function, unicode_literals
__doc__="""
Deletes all annotations in all master layers in all glyphs.
"""

import GlyphsApp, time
Glyphs.clearLog()
print("Delete annotations in all master layers @ " + time.strftime("%H:%M:%S"))

thisFont = Glyphs.font
annotationCounter = 0
for glyph in thisFont.glyphs:
    for layer in glyph.layers:
        if layer.layerId == layer.associatedMasterId:
            for annotation in layer.annotations:
                del(layer.annotations[0])
                annotationCounter += 1

Glyphs.showMacroWindow()
print("%i annotations deleted." % annotationCounter)
