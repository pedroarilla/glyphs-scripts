#MenuTitle: Kerning cleaner
# -*- coding: utf-8 -*-
# by Pedro Arilla
__doc__="""
Removes every kerning pair in the current master between -9 and 9, and rounds the others to base 5.
"""

import GlyphsApp
import time
Glyphs.clearLog()
Glyphs.showMacroWindow()
print "Kerning cleaner @ " + time.strftime("%H:%M:%S")

# Based on "Round metrics to base 5" by @ricardgarcia
def round2Five(number2Round):
	roundedNumber = int(round(number2Round/5.0)*5.0)
	return(roundedNumber)

# Based on "Remove Small Kerning Pairs" by @mekkablue
thisFont = Glyphs.font
thisFontMaster = thisFont.selectedFontMaster
thisFontMasterID = thisFontMaster.id
thisFontMasterKernDict = thisFont.kerning[thisFontMasterID]
kernpairsToBeRemoved = []
kernpairsToBeRounded = []
countZero = 0
countPositive = 0
countNegative = 0
countRound = 0
for leftGlyphID in thisFontMasterKernDict.keys():
    for rightGlyphID in thisFontMasterKernDict[ leftGlyphID ].keys():
        kerningValue = thisFontMasterKernDict[ leftGlyphID ][ rightGlyphID ]
        leftName  = nameForID( thisFont, leftGlyphID )
        rightName = nameForID( thisFont, rightGlyphID )
        if kerningValue == 0.0:
            kernpairsToBeRemoved.append( (leftName, rightName) )
            countZero += 1
        elif 0.0 < kerningValue < 10.0:
            kernpairsToBeRemoved.append( (leftName, rightName) )
            countPositive += 1
        elif 0.0 > kerningValue > -10.0:
            kernpairsToBeRemoved.append( (leftName, rightName) )
            countNegative += 1
        elif kerningValue != round2Five(kerningValue):
            kernpairsToBeRounded.append( (leftName, rightName, kerningValue) )
            countRound += 1
for thisKernPair in kernpairsToBeRemoved:
    leftSide = thisKernPair[0]
    rightSide = thisKernPair[1]
    thisFont.removeKerningForPair( thisFontMasterID, leftSide, rightSide )
for thisKernPair in kernpairsToBeRounded:
    leftSide = thisKernPair[0]
    rightSide = thisKernPair[1]
    kerningValue = round2Five(thisKernPair[2])
    thisFont.setKerningForPair( thisFontMasterID, leftSide, rightSide, kerningValue )
print("Cleaned %i kerning pairs:" % len(kernpairsToBeRemoved))
print("   %i negative pairs removed" % countNegative)
print("   %i zero pairs removed" % countZero)
print("   %i positive pairs removed" % countPositive)
print("   %i kerning pairs rounded" % countRound)
print "Kerning cleaned!"
