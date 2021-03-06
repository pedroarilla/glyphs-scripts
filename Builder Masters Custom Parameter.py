#MenuTitle: Builder: Masters' Custom Parameters
# -*- coding: utf-8 -*-
# by Pedro Arilla
__doc__="""
Sets vertical metrics (win, typo, and hhea values) and strokes (strikeout and underline) across masters.
"""

import GlyphsApp
import vanilla
import time

thisFont = Glyphs.font
yep = "\U00002705"

class verticalMetricsBuilder( object ):
    def __init__( self ):
        # Window 'self.w':
        windowWidth = 430
        windowHeight = 190
        windowWidthResize  = 0 # user can resize width by this value
        windowHeightResize = 0   # user can resize height by this value
        self.w = vanilla.FloatingWindow(
        ( windowWidth, windowHeight ), # default window size
        "Vertical metrics builder", # window title
        minSize = ( windowWidth, windowHeight ), # minimum size (for resizing)
        maxSize = ( windowWidth + windowWidthResize, windowHeight + windowHeightResize ), # maximum size (for resizing)
        autosaveName = "com.pedroarilla.verticalMetricsBuilder.mainwindow" # stores last window position and size
        )

        # UI elements:
        self.w.text_A = vanilla.TextBox( (15, 20, -15, 20), "Top Clipping Point Value", sizeStyle='regular' )
        self.w.edit_A = vanilla.EditText( (350, 20, -15, 20), "", sizeStyle = 'small')
        self.w.text_B = vanilla.TextBox( (15, 50, -15, 20), "Bottom Clipping Point Value (Set as Positive Value)", sizeStyle='regular' )
        self.w.edit_B = vanilla.EditText( (350, 50, -15, 20), "", sizeStyle = 'small')
        self.w.text_C = vanilla.TextBox( (15, 90, -15, 20), ">>> Make sure the total span doesn't exceed 1250 units", sizeStyle='regular' )

        # Run Button:
        self.w.runButton = vanilla.Button((15, 130, -15, 20), "Set Custom Parameters", sizeStyle='regular', callback=self.Main )
        self.w.setDefaultButton( self.w.runButton )

        # Open window and focus on it:
        self.w.open()
        self.w.makeKey()

    def Main( self, sender ):
        try:
            Glyphs.clearLog()
            Glyphs.showMacroWindow()
            print "Builder: Masters' Custom Parameters @ " + time.strftime("%H:%M:%S")
            topValue = self.w.edit_A.get()
            bottomValue = self.w.edit_B.get()
            topValue = int(topValue)
            bottomValue = int(bottomValue)

            # Win
            print "\t# Win values"
            for master in thisFont.masters:
                master.customParameters["winAscent"] = topValue
                master.customParameters["winDescent"] = bottomValue
                print "\t\t" + yep.decode('unicode-escape') + " " + master.name

            # hhea
            print "\t# hhea values"
            for master in thisFont.masters:
                master.customParameters["hheaAscender"] = topValue
                master.customParameters["hheaDescender"] = -bottomValue
                print "\t\t" + yep.decode('unicode-escape') + " " + master.name

            # typo
            print "\t# typo values"
            for master in thisFont.masters:
                master.customParameters["typoAscender"] = master.ascender
                master.customParameters["typoDescender"] = master.descender
                master.customParameters["typoLineGap"] = 200
                print "\t\t" + yep.decode('unicode-escape') + " " + master.name

            # strokes
            print "\t# strokes"
            for master in thisFont.masters:
                master.customParameters["strikeoutPosition"] = 250
                master.customParameters["strikeoutSize"] = 60
                master.customParameters["underlinePosition"] = -100
                master.customParameters["underlineThickness"] = 60
                print "\t\t" + yep.decode('unicode-escape') + " " + master.name

            print "Masters' Custom Parameters set."
            self.w.close() # delete if you want window to stay open

        except:
            print "Error!"

verticalMetricsBuilder()
