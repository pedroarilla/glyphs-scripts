#MenuTitle: Set default figures
# -*- coding: utf-8 -*-
# by Pedro Arilla
from __future__ import division, print_function, unicode_literals
__doc__="""
UI (Vanilla required) for setting the set of numerals selected by the user as default figures. Inserts the figures as components in the ‘Decimal Digit’ cells, enables automatic alignment, and copies kerning groups.
"""

import GlyphsApp, time, vanilla

class setDefaultFigures( object ):
	def __init__( self ):
		windowWidth  = 240
		windowHeight = 200
		windowWidthResize  = 0 # user can resize width by this value
		windowHeightResize = 0 # user can resize height by this value
		self.w = vanilla.FloatingWindow(
			( windowWidth, windowHeight ), # default window size
			"Set default figures", # window title
			minSize = ( windowWidth, windowHeight ), # minimum size (for resizing)
			maxSize = ( windowWidth + windowWidthResize, windowHeight + windowHeightResize ), # maximum size (for resizing)
			autosaveName = "com.pedroarilla.setDefaultFigures.mainwindow" # stores last window position and size
		)

		# UI elements:
		self.w.text = vanilla.TextBox( (15, 20, -15, 20), "Choose set of figures:", sizeStyle='regular' )
		self.w.optionFigures = vanilla.RadioGroup( (35, 50, -15, 20*4), ["Lining figures", "Old style figures", "Tabular lining figures", "Tabular old style figures"], isVertical = True, sizeStyle='regular', callback=self.SavePreferences )

		# Run Button:
		self.w.runButton = vanilla.Button( (-240+15, -20-15, -15, -15), "Set default figures", sizeStyle='regular', callback=self.setDefaultFiguresMain )
		self.w.setDefaultButton( self.w.runButton )

		# Load Settings:
		if not self.LoadPreferences():
			print("Note: 'Set default figures' could not load preferences. Will resort to defaults")

		# Open window and focus on it:
		self.w.open()
		self.w.makeKey()

	def SavePreferences( self, sender ):
		try:
			Glyphs.defaults["com.pedroarilla.setDefaultFigures.optionFigures"] = self.w.optionFigures.get()
		except:
			return False
		return True

	def LoadPreferences( self ):
		try:
			NSUserDefaults.standardUserDefaults().registerDefaults_(
				{
					"com.pedroarilla.setDefaultFigures.optionFigures": 0,
				}
			)
			self.w.optionFigures.set( Glyphs.defaults["com.pedroarilla.setDefaultFigures.optionFigures"] )
		except:
			return False
		return True

	def setDefaultFiguresMain( self, sender ):
		try:
			Glyphs.clearLog()
			print("Set default figures @ " + time.strftime("%H:%M:%S"))
			thisFont = Glyphs.font
			defaultFigures = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
			liningFigures = ["zero.lf", "one.lf", "two.lf", "three.lf", "four.lf", "five.lf", "six.lf", "seven.lf", "eight.lf", "nine.lf"]
			oldStyleFigures = ["zero.osf", "one.osf", "two.osf", "three.osf", "four.osf", "five.osf", "six.osf", "seven.osf", "eight.osf", "nine.osf"]
			tabularFigures = ["zero.tf", "one.tf", "two.tf", "three.tf", "four.tf", "five.tf", "six.tf", "seven.tf", "eight.tf", "nine.tf"]
			tabularOldFigures = ["zero.tosf", "one.tosf", "two.tosf", "three.tosf", "four.tosf", "five.tosf", "six.tosf", "seven.tosf", "eight.tosf", "nine.tosf"]

			# User selection:
			if Glyphs.defaults["com.pedroarilla.setDefaultFigures.optionFigures"] == 0:
				sourceFigures = liningFigures
			elif Glyphs.defaults["com.pedroarilla.setDefaultFigures.optionFigures"] == 1:
				sourceFigures = oldStyleFigures
			elif Glyphs.defaults["com.pedroarilla.setDefaultFigures.optionFigures"] == 2:
				sourceFigures = tabularFigures
			elif Glyphs.defaults["com.pedroarilla.setDefaultFigures.optionFigures"] == 3:
				sourceFigures = tabularOldFigures

			# Setting default figures:
			for i in defaultFigures:
				targetNumber = thisFont.glyphs[i]
				sourceNumber = thisFont.glyphs[sourceFigures[defaultFigures.index(i)]]
				for master in thisFont.masters:
					masterLayer = targetNumber.layers[master.id]
					masterLayer.components = [GSComponent(sourceNumber)]
					for thisComponent in masterLayer.components:
						thisComponent.setDisableAlignment_( False )
				targetNumber.leftKerningGroup = sourceNumber.leftKerningGroup
				targetNumber.rightKerningGroup = sourceNumber.rightKerningGroup

			print("Default figures set succesfully.")

			if not self.SavePreferences( self ):
				print("Note: 'Set default figures' could not write preferences.")

			self.w.close() # delete if you want window to stay open

		except Exception as e:
			# brings macro window to front and reports error:
			Glyphs.clearLog()
			print("Set default figures @ " + time.strftime("%H:%M:%S"))
			Glyphs.showMacroWindow()
			print("Set default figures Error: %s" % e)
			import traceback
			print(traceback.format_exc())

setDefaultFigures()
