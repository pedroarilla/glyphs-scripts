#MenuTitle: Select small paths
# -*- coding: utf-8 -*-
# by Pedro Arilla
from __future__ import division, print_function, unicode_literals
__doc__="""
Finds and selects small paths (smaller than a user-definable area) in the current glyph.
"""

import GlyphsApp, time
from robofab.interface.all.dialogs import AskString
Glyphs.clearLog()
print("Select small paths @ " + time.strftime("%H:%M:%S"))

def is_a_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

minArea = AskString("Select paths with an area smaller than (in square units)")
if not is_a_number(minArea):
	Glyphs.showMacroWindow()
	print("Error: Not a number")
else:
	minArea = float(minArea)
	pathCounter = 0
	thisFont = Glyphs.font
	currentLayer = thisFont.selectedLayers[0]
	thisFont.disableUpdateInterface()
	currentLayer.clearSelection()
	currentGlyph = currentLayer.parent
	currentGlyph.beginUndo()
	for path in currentLayer.paths:
		if path.area() < minArea:
			for thisNode in path.nodes:
				currentLayer.addSelection_(thisNode)
			pathCounter += 1
	currentGlyph.endUndo()
	thisFont.enableUpdateInterface()
	print("%i paths selected." % pathCounter)
