#MenuTitle: Select partial path
# -*- coding: utf-8 -*-
# by Pedro Arilla
__doc__="""
Selects the partial path between the selected nodes in the current glyph — take into account that the script goes through the path starting from the first node.

Recommended keyboard shortcut: Cmd+Ctrl+A
[via Mac OS System Preferences > Keyboard > Shortcuts > App Shortcuts > Glyphs.app]
"""

import GlyphsApp
import time
Glyphs.clearLog()
print "Select partial path @ " + time.strftime("%H:%M:%S")

thisFont = Glyphs.font
currentLayer = thisFont.selectedLayers[0]
currentGlyph = currentLayer.parent
partialPath = False
thisFont.disableUpdateInterface()
currentGlyph.beginUndo()
for path in currentLayer.paths:
    for node in path.nodes:
        if node.selected:
            currentLayer.addSelection_(node)
            partialPath = not partialPath
        elif partialPath:
            currentLayer.addSelection_(node)
currentGlyph.endUndo()
thisFont.enableUpdateInterface()

print "Partial path selected."
