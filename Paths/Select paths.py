#MenuTitle: Select paths
# -*- coding: utf-8 -*-
# by Pedro Arilla
from __future__ import division, print_function, unicode_literals
__doc__="""
Selects the path or paths you are working on—according to the selected nodes.

Recommended keyboard shortcut: Cmd+Shift+A
[via Mac OS System Preferences > Keyboard > Shortcuts > App Shortcuts > Glyphs.app]
"""

import GlyphsApp
import time
Glyphs.clearLog()
print("Select paths @ " + time.strftime("%H:%M:%S"))

thisFont = Glyphs.font
currentLayer = thisFont.selectedLayers[0]
currentGlyph = currentLayer.parent
thisFont.disableUpdateInterface()
currentGlyph.beginUndo()
for path in currentLayer.paths:
    selectable = False
    for node in path.nodes:
        if node.selected:
            selectable = True
            break
    if selectable:
        for node in path.nodes:
            currentLayer.addSelection_(node)
currentGlyph.endUndo()
thisFont.enableUpdateInterface()

print("Paths selected.")
