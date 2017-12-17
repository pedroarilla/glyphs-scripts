#MenuTitle: Selection to global background
# -*- coding: utf-8 -*-
# by Pedro Arilla
__doc__="""
Replaces on all the glyphs the current content of the background with the selected paths.

Recommended keyboard shortcut: Cmd+Shift+J
[via Mac OS System Preferences > Keyboard > Shortcuts > App Shortcuts > Glyphs.app]
"""

import GlyphsApp

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

Glyphs.clearLog()
print "Global background assigned."
