#MenuTitle: Make zero-handles selected nodes
# -*- coding: utf-8 -*-
# by Pedro Arilla
__doc__="""
Makes zero-length all handles (overlapping nodes) in selected nodes.
"""

import GlyphsApp
import time
Glyphs.clearLog()
print "Make zero-handles selected nodes @ " + time.strftime("%H:%M:%S")

i = 0
thisFont = Glyphs.font
thisFont.disableUpdateInterface()
thisLayer = thisFont.selectedLayers[0]
for thisPath in thisLayer.paths:
    for thisNode in thisPath.nodes:
        if thisNode.type != GSOFFCURVE:
            if thisNode.selected:
                before = i - 1
                after = i + 1
                if thisPath.nodes[before].type == GSOFFCURVE:
                    thisPath.nodes[before].x = thisPath.nodes[i].x
                    thisPath.nodes[before].y = thisPath.nodes[i].y
                if thisPath.nodes[after].type == GSOFFCURVE:
                    thisPath.nodes[after].x = thisPath.nodes[i].x
                    thisPath.nodes[after].y = thisPath.nodes[i].y
        i += 1
thisFont.enableUpdateInterface()
print "Zero-handles nodes made in selected nodes."
