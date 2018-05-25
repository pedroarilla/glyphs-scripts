#MenuTitle: Simplify selection
# -*- coding: utf-8 -*-
# by Pedro Arilla
__doc__="""
Simplifies the selected path(s) by deleting one of every two nodes.
"""

import GlyphsApp
import time
Glyphs.clearLog()
print "Simplify selection @ " + time.strftime("%H:%M:%S")

thisFont = Glyphs.font
selection = thisFont.selectedLayers[0].selection
delete = False
thisFont.disableUpdateInterface()
for thisNode in selection:
    if delete:
        thisNode.parent.removeNodeCheckKeepShape_( thisNode )
    delete = not delete
thisFont.enableUpdateInterface()

print "Path(s) simplified."
