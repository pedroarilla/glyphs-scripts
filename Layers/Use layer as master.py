#MenuTitle: Use layer as master
# -*- coding: utf-8 -*-
# by Pedro Arilla
from __future__ import division, print_function, unicode_literals
__doc__="""
Sets the current layer as the master layer.
"""

import GlyphsApp, time
Glyphs.clearLog()
print("Use layer as master @ " + time.strftime("%H:%M:%S"))

thisFont = Glyphs.font
thisLayer = thisFont.selectedLayers[0]
thisGlyph = thisLayer.parent
if not thisLayer.layerId == thisLayer.associatedMasterId:
	thisFont.disableUpdateInterface()
	# Make a copy of the master layer:
	masterLayer = thisGlyph.layers[thisLayer.associatedMasterId]
	newLayer = masterLayer.copy()
	newLayer.name = '@ '+ time.strftime("%H:%M, %d/%m/%y")
	thisFont.glyphs[thisGlyph.name].layers.append(newLayer)
	# Copy this layer content to the master layer:
	masterLayer.setBackground_( thisLayer.background )
	masterLayer.setPaths_( None )
	for thisPath in thisLayer.paths:
		newPath = thisPath.copy()
		masterLayer.paths.append( newPath )
	masterLayer.setComponents_( None )
	for thisComponent in thisLayer.components:
		newComponent = thisComponent.copy()
		masterLayer.components.append( newComponent )
	masterLayer.setAnchors_( None )
	for thisAnchor in thisLayer.anchors:
		newAnchor = thisAnchor.copy()
		masterLayer.anchors.append( newAnchor )
	masterLayer.leftMetricsKey = thisLayer.leftMetricsKey
	masterLayer.rightMetricsKey = thisLayer.rightMetricsKey
	# Delete this layer:
	thisGlyph.beginUndo()
	del thisGlyph.layers[thisLayer.layerId]
	thisGlyph.endUndo()
	thisFont.enableUpdateInterface()
	print("Layer set as master.")
else: print("Error: current layer is already the master layer.")
