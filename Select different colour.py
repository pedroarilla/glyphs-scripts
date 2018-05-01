#MenuTitle: Select different colour
# -*- coding: utf-8 -*-
# Based on _Select Different Color_ by Rainer Erich Scheichelbauer (@mekkablue)
# Modified by Pedro Arilla
__doc__="""
In Font view, selects glyphs with a different colour as the currently selected one(s).
"""

import GlyphsApp
import time
Glyphs.clearLog()
print "Select different colour @ " + time.strftime("%H:%M:%S")

from AppKit import NSIndexSet

def indexSetWithIndex( index ):
	indexSet = NSIndexSet.alloc().initWithIndex_( index )
	return indexSet

thisDoc = Glyphs.currentDocument # frontmost document
try:
	fontView = thisDoc.windowController().tabBarControl().tabItemAtIndex_(0).glyphsArrayController()
except:
	fontView = thisDoc.windowController().tabBarControl().viewControllers()[0].glyphsArrayController()
displayedGlyphsInFontView = fontView.arrangedObjects() # all glyphs currently displayed
colorIndexes = []

if displayedGlyphsInFontView:
	displayedIndexRange = range(len(displayedGlyphsInFontView)) # indexes of glyphs in Font view
	for i in displayedIndexRange:
		if fontView.selectionIndexes().containsIndex_(i):
			thisGlyphColorIndex = displayedGlyphsInFontView[i].colorIndex()
			if not thisGlyphColorIndex in colorIndexes:
				colorIndexes.append( thisGlyphColorIndex )
	if colorIndexes:
		for i in displayedIndexRange:
			if not displayedGlyphsInFontView[i].colorIndex() in colorIndexes:
				fontView.addSelectionIndexes_( indexSetWithIndex(i) )

print "Select different colour."
