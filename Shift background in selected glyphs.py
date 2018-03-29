#MenuTitle: Shift background in selected glyphs
# -*- coding: utf-8 -*-
# by Pedro Arilla
__doc__="""
Shifts horizontally (user-definable number) the background content in selected glyphs. Positive value for shifting to the right, negative value for shifting to the left.
"""

import GlyphsApp
from robofab.interface.all.dialogs import AskString
import time
Glyphs.clearLog()
print "Shift background in selected glyphs @ " + time.strftime("%H:%M:%S")

def is_a_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

shift = AskString("Shift background content in (number as units)")
if not is_a_number(shift):
	Glyphs.showMacroWindow()
	print "Error: Not a number"
else:
    shift = float(shift)
    thisFont = Glyphs.font
    listOfSelectedLayers = thisFont.selectedLayers
    thisFont.disableUpdateInterface()
    for thisLayer in listOfSelectedLayers:
        for comp in thisLayer.background.components:
            pos = comp.position
            pos.x = pos.x + shift
            comp.position = pos
        for path in thisLayer.background.paths:
            for node in path.nodes:
                pos = node.position
                pos.x = pos.x + shift
                node.position = pos
    thisFont.enableUpdateInterface()
print "Backgrounds shifted."
