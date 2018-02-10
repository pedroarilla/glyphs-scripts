#MenuTitle: Display previous layer
# -*- coding: utf-8 -*-
# by Pedro Arilla
__doc__="""
Switches to the previous layer of the current glyph within the current master.

Recommended keyboard shortcut: Ctrl+DownUp
[via Mac OS System Preferences > Keyboard > Shortcuts > App Shortcuts > Glyphs.app]
"""

import GlyphsApp
import time
Glyphs.clearLog()
print "Display previous layer @ " + time.strftime("%H:%M:%S")

layersList = []
thisFont = Glyphs.font
currentTab = thisFont.currentTab
if thisFont and currentTab:
	currentLayer = currentTab.activeLayer()
	currentMasterId = currentLayer.associatedMasterId
	currentGlyph = currentLayer.parent
	# list of layers within the master
	currentIndex = 0
	i = 0
	for layer in currentGlyph.layers:
		if layer.associatedMasterId == currentMasterId:
			layersList.append(layer.layerId)
			if currentLayer.layerId == layer.layerId:
				currentIndex = i
			i += 1
	# switch to next layer
	nextIndex = (currentIndex-1)%len(layersList)
	nextLayer = layersList[nextIndex]
	nextLayerData = NSMutableAttributedString.alloc().init()
	glyphUni = thisFont.characterForGlyph_( currentGlyph )
	tempData = NSAttributedString.alloc().initWithString_attributes_( unichr(glyphUni), { "GSLayerIdAttrib" : nextLayer } )
	nextLayerData.appendAttributedString_( tempData )
	currentTab.layers._owner.graphicView().textStorage().setText_(nextLayerData)
print "Next previous active."
