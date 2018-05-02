#MenuTitle: Decompose all serif components
# -*- coding: utf-8 -*-
# by Pedro Arilla
__doc__="""
Decomposes all serif components in selected glyphs.
"""
import GlyphsApp
import time
Glyphs.clearLog()
print "Decompose all serif components @ " + time.strftime("%H:%M:%S")

thisFont = Glyphs.font
for thisLayer in thisFont.selectedLayers:
	for i in range(len(thisLayer.components))[::-1]:
		if thisLayer.components[i].componentName.startswith("Serif"):
			thisLayer.components[i].decompose()

print "All serif components decomposed."
