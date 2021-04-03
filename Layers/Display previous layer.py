#MenuTitle: Display previous layer
# -*- coding: utf-8 -*-
# by Pedro Arilla
from __future__ import division, print_function, unicode_literals
__doc__="""
Switches to the previous layer of the current glyph within the current master.
"""

import GlyphsApp, time
Glyphs.clearLog()
print("Display previous layer @ " + time.strftime("%H:%M:%S"))

layersList = []
thisFont = Glyphs.font
currentTab = thisFont.currentTab
if thisFont and currentTab:
	currentLayer = currentTab.activeLayer()
	currentMasterId = currentLayer.associatedMasterId
	currentGlyph = currentLayer.parent
	# Find the actual layer-cursor position:
	currentIndex = 0
	i = 0
	for layer in currentGlyph.layers:
		if layer.associatedMasterId == currentMasterId:
			layersList.append(layer.layerId)
			if currentLayer.layerId == layer.layerId:
				currentIndex = i
			i += 1
	# Previous layer data:
	previousIndex = (currentIndex-1)%len(layersList)
	previousLayer = layersList[previousIndex]
	# Switch to previous layer:
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
			singleChar = NSAttributedString.alloc().initWithString_attributes_( unichr(char), { "GSLayerIdAttrib" : previousLayer } )
		else:
			singleChar = NSAttributedString.alloc().initWithString_attributes_( unichr(char), { "GSLayerIdAttrib" : layer.layerId } )
		string.appendAttributedString_( singleChar )
	currentTab.layers._owner.graphicView().textStorage().setText_(string)
print("Previous layer active.")
