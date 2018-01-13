#MenuTitle: Display next layer
# -*- coding: utf-8 -*-
# slightly adapted by Pedro Arilla from a @mekkablue's (Rainer Erich Scheichelbauer) snippet
# source: https://forum.glyphsapp.com/t/keyboard-shortcuts-for-the-layers-palette/6578/2
__doc__="""
Switches to the next layer of the current glyph.

Recommended keyboard shortcut: Ctrl+DownArrow
[via Mac OS System Preferences > Keyboard > Shortcuts > App Shortcuts > Glyphs.app]
"""

import GlyphsApp
thisFont = Glyphs.font
currentTab = thisFont.currentTab

if thisFont and currentTab:
	currentLayer = currentTab.activeLayer()
	if currentLayer:
		currentGlyph = currentLayer.parent
		availableLayers = currentGlyph.layers
		currentIndex = availableLayers.index(currentLayer)
		nextIndex = (currentIndex+1)%len(availableLayers)
		nextLayer = availableLayers[nextIndex]
		offset = currentTab.layersCursor
		newLayers = currentTab.layers[:]
		newLayers.insert(offset,nextLayer)
		newLayers.pop(offset+1)
		currentTab.layers = newLayers

Glyphs.clearLog()
print "Next layer active."
