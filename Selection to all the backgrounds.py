#MenuTitle: Selection to all the backgrounds
# -*- coding: utf-8 -*-
# by Pedro Arilla
__doc__="""
Replaces in all the glyphs their current content of the background with the selected paths of the current glyph.

Recommended keyboard shortcut: Cmd+Shift+J
[via Mac OS System Preferences > Keyboard > Shortcuts > App Shortcuts > Glyphs.app]
"""

import GlyphsApp
import time
Glyphs.clearLog()
print "Selection to all the backgrounds @ " + time.strftime("%H:%M:%S")

thisFont = Glyphs.font
thisFont.disableUpdateInterface()
currentLayer = thisFont.selectedLayers[0]
currentLayer.setBackground_( None )
for path in currentLayer.paths:
	if path.selected:
		currentLayer.background.paths.append( path.copy() )
for glyph in thisFont.glyphs:
	glyph.layers[thisFont.selectedFontMaster.id].setBackground_( currentLayer.background )
thisFont.enableUpdateInterface()

print "Global background assigned."
