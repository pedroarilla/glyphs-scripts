#MenuTitle: Make zero-handles selected glyphs
# -*- coding: utf-8 -*-
# by Pedro Arilla
__doc__="""
Makes zero-length all handles (overlapping nodes) in selected glyphs.
"""

import GlyphsApp
import time
Glyphs.clearLog()
print "Make zero-handles selected glyphs @ " + time.strftime("%H:%M:%S")

i = 0
previous = True
thisFont = Glyphs.font
thisFont.disableUpdateInterface()
for thisLayer in thisFont.selectedLayers:
    for thisPath in thisLayer.paths:
        for thisNode in thisPath.nodes:
            if thisNode.type == GSOFFCURVE:
                if previous:
                    nodeIndex = i - 1
                    thisPath.nodes[i].x = thisPath.nodes[nodeIndex].x
                    thisPath.nodes[i].y = thisPath.nodes[nodeIndex].y
                else:
                    nodeIndex = i + 1
                    thisPath.nodes[i].x = thisPath.nodes[nodeIndex].x
                    thisPath.nodes[i].y = thisPath.nodes[nodeIndex].y
                previous = False
            else:
                previous = True
            i += 1
thisFont.enableUpdateInterface()
print "Zero-handles nodes made in selected glyphs."
