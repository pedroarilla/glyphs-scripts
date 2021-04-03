#MenuTitle: Decompose all corner components
# -*- coding: utf-8 -*-
# by Pedro Arilla
from __future__ import division, print_function, unicode_literals
__doc__="""
Decomposes all corner components in selected glyphs.
"""
import GlyphsApp, time
Glyphs.clearLog()
print("Decompose all corner components @ " + time.strftime("%H:%M:%S"))

thisFont = Glyphs.font
for thisLayer in thisFont.selectedLayers:
	thisLayer.decomposeCorners()

print("All corner components decomposed.")
