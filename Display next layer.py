#MenuTitle: Display next layer
# -*- coding: utf-8 -*-
# by Pedro Arilla
__doc__="""
Switches to the next layer of the current glyph within the current master.

Recommended keyboard shortcut: Ctrl+DownArrow
[via Mac OS System Preferences > Keyboard > Shortcuts > App Shortcuts > Glyphs.app]
"""

import GlyphsApp
import time
Glyphs.clearLog()
print "Display next layer @ " + time.strftime("%H:%M:%S")

layersList = []
thisFont = Glyphs.font
currentTab = thisFont.currentTab
if thisFont and currentTab:
	currentLayer = currentTab.activeLayer()
	currentMasterId = currentLayer.associatedMasterId
	currentGlyph = currentLayer.parent
	# Find the actual cursor position:
	currentIndex = 0
	i = 0
	for layer in currentGlyph.layers:
		if layer.associatedMasterId == currentMasterId:
			layersList.append(layer.layerId)
			if currentLayer.layerId == layer.layerId:
				currentIndex = i
			i += 1
	# Next layer data:
	nextIndex = (currentIndex+1)%len(layersList)
	nextLayer = layersList[nextIndex]
	# Switch to next layer:
	layers = currentTab.layers.values()
	string = NSMutableAttributedString.alloc().init()
	for i in xrange( len( layers ) ):
		layer = layers[i]
		try:
			char = thisFont.characterForGlyph_( layer.parent )
		except:
			continue
		singleChar = NSAttributedString.alloc().initWithString_attributes_( unichr(char), {} )
		if i == currentTab.layersCursor:
			singleChar = NSAttributedString.alloc().initWithString_attributes_( unichr(char), { "GSLayerIdAttrib" : nextLayer } )
		else:
			singleChar = NSAttributedString.alloc().initWithString_attributes_( unichr(char), { "GSLayerIdAttrib" : layer.layerId } )
		string.appendAttributedString_( singleChar )
	currentTab.layers._owner.graphicView().textStorage().setText_(string)
print "Next layer active."
