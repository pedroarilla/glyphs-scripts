#MenuTitle: Scale background in selected glyphs
# -*- coding: utf-8 -*-
# by Pedro Arilla
from __future__ import division, print_function, unicode_literals
__doc__="""
Scales proportionally (user-definable percentage) the background content in selected glyphs.
"""

import GlyphsApp, time, vanilla
Glyphs.clearLog()
print("Scale background in selected glyphs @ " + time.strftime("%H:%M:%S"))

class scaleBackground( object ):
    def __init__( self ):
        # Window 'self.w':
        windowWidth = 480
        windowHeight = 115
        windowWidthResize  = 0 # user can resize width by this value
        windowHeightResize = 0   # user can resize height by this value
        self.w = vanilla.FloatingWindow(
        ( windowWidth, windowHeight ), # default window size
        "Scale background", # window title
        minSize = ( windowWidth, windowHeight ), # minimum size (for resizing)
        maxSize = ( windowWidth + windowWidthResize, windowHeight + windowHeightResize ), # maximum size (for resizing)
        autosaveName = "com.pedroarilla.scaleBackground.mainwindow" # stores last window position and size
        )

        # UI elements:
        self.w.text_A = vanilla.TextBox( (15, 20, -15, 20), "Scale background content to [X]% — enter X as an integer:", sizeStyle='regular' )
        self.w.edit_A = vanilla.EditText( (400, 20, -20, 20), "", sizeStyle = 'small')

        # Run Button:
        self.w.runButton = vanilla.Button((15, 60, -15, 20), "Escale background", sizeStyle='regular', callback=self.Main )
        self.w.setDefaultButton( self.w.runButton )

        # Open window and focus on it:
        self.w.open()
        self.w.makeKey()

    def is_a_number(number):
        try:
            float(number)
            return True
        except ValueError:
            return False

    def Main( self, sender ):
        try:
            scale = self.w.edit_A.get()
            if not is_a_number(scale):
            	Glyphs.showMacroWindow()
            	print("Error: Not a number")
            else:
                scale = float(scale) * 0.01
                thisFont = Glyphs.font
                listOfSelectedLayers = thisFont.selectedLayers
                thisFont.disableUpdateInterface()
                for thisLayer in listOfSelectedLayers:
                    for path in thisLayer.background.paths:
                        for node in path.nodes:
                            pos = node.position
                            pos.x = pos.x * scale
                            pos.y = pos.y * scale
                            node.position = pos
                thisFont.enableUpdateInterface()
            print("Backgrounds scaled.")
            self.w.close() # delete if you want window to stay open
        except:
            print("Error!")

scaleBackground()
