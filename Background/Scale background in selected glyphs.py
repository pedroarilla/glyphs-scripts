#MenuTitle: Scale background in selected glyphs
# -*- coding: utf-8 -*-
# by Pedro Arilla
__doc__="""
Scales proportionally (user-definable percentage) the background content in selected glyphs.
"""

import GlyphsApp
from robofab.interface.all.dialogs import AskString
import time
Glyphs.clearLog()
print "Scale background in selected glyphs @ " + time.strftime("%H:%M:%S")

def is_a_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

scale = AskString("Scale background content in (number as percentage)")
if not is_a_number(scale):
	Glyphs.showMacroWindow()
	print "Error: Not a number"
else:
    scale = float(scale) * 0.01
    thisFont = Glyphs.font
    listOfSelectedLayers = thisFont.selectedLayers
    thisFont.disableUpdateInterface()
    for thisLayer in listOfSelectedLayers:
        for path in thisLayer.background.paths:
            for node in path.nodes:
                pos = node.position
                pos.x = pos.x * scale
                pos.y = pos.y * scale
                node.position = pos
    thisFont.enableUpdateInterface()
print "Backgrounds scaled."
