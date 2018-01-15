#MenuTitle: Select partial path
# -*- coding: utf-8 -*-
# by Pedro Arilla
__doc__="""
Selects the partial path between the selected nodes in the current glyph — take into account that the script goes through the path starting from the first node.

Recommended keyboard shortcut: Cmd+Ctrl+A
[via Mac OS System Preferences > Keyboard > Shortcuts > App Shortcuts > Glyphs.app]
"""

import GlyphsApp
Glyphs.clearLog()
thisFont = Glyphs.font
currentLayer = thisFont.selectedLayers[0]
currentGlyph = currentLayer.parent
partialPath = False

thisFont.disableUpdateInterface()
currentGlyph.beginUndo()
for thisPath in currentLayer.paths:
    for thisNode in thisPath.nodes:
        if thisNode.selected:
            currentLayer.addSelection_(thisNode)
            partialPath = not partialPath
        elif partialPath:
            currentLayer.addSelection_(thisNode)
currentGlyph.endUndo()
thisFont.enableUpdateInterface()

print "Partial path selected."
