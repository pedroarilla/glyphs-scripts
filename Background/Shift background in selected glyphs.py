#MenuTitle: Shift background in selected glyphs
# -*- coding: utf-8 -*-
# by Pedro Arilla
from __future__ import division, print_function, unicode_literals
__doc__="""
Shifts horizontally (user-definable number) the background content in selected glyphs. Positive value for shifting to the right, negative value for shifting to the left.
"""

import GlyphsApp, vanilla, time
Glyphs.clearLog()
print("Shift background in selected glyphs @ " + time.strftime("%H:%M:%S"))

class shiftBackground( object ):
    def __init__( self ):
        # Window 'self.w':
        windowWidth = 480
        windowHeight = 140
        windowWidthResize  = 0 # user can resize width by this value
        windowHeightResize = 0   # user can resize height by this value
        self.w = vanilla.FloatingWindow(
        ( windowWidth, windowHeight ), # default window size
        "Shift background", # window title
        minSize = ( windowWidth, windowHeight ), # minimum size (for resizing)
        maxSize = ( windowWidth + windowWidthResize, windowHeight + windowHeightResize ), # maximum size (for resizing)
        autosaveName = "com.pedroarilla.shiftBackground.mainwindow" # stores last window position and size
        )

        # UI elements:
        self.w.text_A = vanilla.TextBox( (15, 20, -15, 20), "Shift background content in [X] units — enter X as an integer", sizeStyle='regular' )
        self.w.edit_A = vanilla.EditText( (400, 20, -20, 20), "", sizeStyle = 'small')
        self.w.text_B = vanilla.TextBox( (15, 50, -15, 20), "ℹ️ Negative value = Shift to the left; Positive value = Shift to the right", sizeStyle='regular' )

        # Run Button:
        self.w.runButton = vanilla.Button((15, 85, -15, 20), "Shift background", sizeStyle='regular', callback=self.Main )
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
            shift = self.w.edit_A.get()
            if not is_a_number(shift):
            	Glyphs.showMacroWindow()
            	print("Error: Not a number")
            else:
                shift = float(shift)
                thisFont = Glyphs.font
                listOfSelectedLayers = thisFont.selectedLayers
                thisFont.disableUpdateInterface()
                for thisLayer in listOfSelectedLayers:
                    for comp in thisLayer.background.components:
                        pos = comp.position
                        pos.x = pos.x + shift
                        comp.position = pos
                    for path in thisLayer.background.paths:
                        for node in path.nodes:
                            pos = node.position
                            pos.x = pos.x + shift
                            node.position = pos
                thisFont.enableUpdateInterface()
            print("Backgrounds shifted.")
            self.w.close() # delete if you want window to stay open
        except:
            print("Error!")

shiftBackground()
