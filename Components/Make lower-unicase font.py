#MenuTitle: Make lower-unicase font
# encoding: utf-8
# Based on _Make Unicase Font_ by Georg Seifert (@schriftgestalt)
# Modified by Pedro Arilla
from __future__ import division, print_function, unicode_literals
__doc__="""
Makes a lower-unicase font placing the lowercase glyphs (as components) in the uppercasse cells.
"""
import GlyphsApp, time
Glyphs.clearLog()
print("Make lower-unicase font @ " + time.strftime("%H:%M:%S"))

thisFont = Glyphs.font
allGlyphs = list(thisFont.glyphs)
for lowerGlyph in allGlyphs:
	if lowerGlyph.category == "Letter" and lowerGlyph.subCategory == "Lowercase":
		upperName = lowerGlyph.name.title()
		print("\tUpper", upperName)
		upperGlyph = thisFont.glyphs[upperName]
		if not upperGlyph:
			upperGlyph = GSGlyph(upperName)
			thisFont.glyphs.append(upperGlyph)
		for master in thisFont.masters:
			layer = upperGlyph.layers[master.id]
			layer.paths = []
			for k in layer.anchors.keys():
				del(layer.anchors[str(k)])
			layer.components = [GSComponent(lowerGlyph.name)]
		upperGlyph.leftKerningGroup = lowerGlyph.leftKerningGroup
		upperGlyph.rightKerningGroup = lowerGlyph.rightKerningGroup
print("Lower-unicase font made.")
