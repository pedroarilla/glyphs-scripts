#MenuTitle: Duplicate current layer
# -*- coding: utf-8 -*-
# by Pedro Arilla
__doc__="""
Duplicates the current layer as a normal glyph layer.

Recommended keyboard shortcut: Cmd+Shift+D
[via Mac OS System Preferences > Keyboard > Shortcuts > App Shortcuts > Glyphs.app]
"""

import GlyphsApp
import time
Glyphs.clearLog()
print "Duplicate current layer @ " + time.strftime("%H:%M:%S")

thisFont = Glyphs.font
currentLayer = thisFont.selectedLayers[0]
currentGlyph = currentLayer.parent
newLayer = currentLayer.copy()
newLayer.name = '@ '+ time.strftime("%H:%M, %d/%m/%y")
thisFont.glyphs[currentGlyph.name].layers.append(newLayer)

print "Layer duplicated."
