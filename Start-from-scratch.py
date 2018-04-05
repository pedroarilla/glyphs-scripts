#MenuTitle: Start-from-scratch
# -*- coding: utf-8 -*-
# by Pedro Arilla
__doc__="""
UI for deleting anchors, annotations, backgrounds, guidelines, images, kerning groups, labels, metric keys, non-master layers, and paths and components—in selected/all the glyphs, selected/all the masters, and master/all the layers.
"""

import GlyphsApp
import time
import vanilla

class startFromScratch( object ):
	def __init__( self ):
		windowWidth  = 240
		windowHeight = 560
		windowWidthResize  = 0 # user can resize width by this value
		windowHeightResize = 0 # user can resize height by this value
		self.w = vanilla.FloatingWindow(
			( windowWidth, windowHeight ), # default window size
			"Start-from-scratch", # window title
			minSize = ( windowWidth, windowHeight ), # minimum size (for resizing)
			maxSize = ( windowWidth + windowWidthResize, windowHeight + windowHeightResize ), # maximum size (for resizing)
			autosaveName = "com.pedroarilla.StartFromScratch.mainwindow" # stores last window position and size
		)

		# UI elements:
		self.w.text_1 = vanilla.TextBox( (15, 20*1, -15, 20), "Delete:", sizeStyle='regular' )
		self.w.cleanAnchors = vanilla.CheckBox( (15, 20*2+10, -15, 20), "Anchors", value=False, callback=self.SavePreferences, sizeStyle='regular' )
		self.w.cleanAnnotations = vanilla.CheckBox( (15, 20*3+10, -15, 20), "Annotations", value=False, callback=self.SavePreferences, sizeStyle='regular' )
		self.w.cleanBackgrounds = vanilla.CheckBox( (15, 20*4+10, -15, 20), "Backgrounds", value=False, callback=self.SavePreferences, sizeStyle='regular' )
		self.w.cleanGuidelines = vanilla.CheckBox( (15, 20*5+10, -15, 20), "Guidelines", value=False, callback=self.SavePreferences, sizeStyle='regular' )
		self.w.cleanImages = vanilla.CheckBox( (15, 20*6+10, -15, 20), "Images", value=False, callback=self.SavePreferences, sizeStyle='regular' )
		self.w.cleanKerning = vanilla.CheckBox( (15, 20*7+10, -15, 20), "Kerning groups", value=False, callback=self.SavePreferences, sizeStyle='regular' )
		self.w.cleanLabels = vanilla.CheckBox( (15, 20*8+10, -15, 20), "Labels", value=False, callback=self.SavePreferences, sizeStyle='regular' )
		self.w.cleanMetrics = vanilla.CheckBox( (15, 20*9+10, -15, 20), "Metric keys", value=False, callback=self.SavePreferences, sizeStyle='regular' )
		self.w.cleanLayers = vanilla.CheckBox( (15, 20*10+10, -15, 20), "Non-master layers", value=False, callback=self.SavePreferences, sizeStyle='regular' )
		self.w.cleanPaths = vanilla.CheckBox( (15, 20*11+10, -15, 20), "Paths and components", value=False, callback=self.SavePreferences, sizeStyle='regular' )

		self.w.text_2 = vanilla.TextBox( (15, 20*13, -15, 20), "Apply to glyphs:", sizeStyle='regular' )
		self.w.applyToGlyphs = vanilla.RadioGroup( (35, 20*14+10, -15, 20*2), ["Only selected glyphs", "All the glyphs in font"], isVertical = True, sizeStyle='regular', callback=self.SavePreferences )

		self.w.text_3 = vanilla.TextBox( (15, 20*17, -15, 20), "Apply to masters:", sizeStyle='regular' )
		self.w.applyToMasters = vanilla.RadioGroup( (35, 20*18+10, -15, 20*2), ["Only selected master", "All the masters"], isVertical = True, sizeStyle='regular', callback=self.SavePreferences )

		self.w.text_4 = vanilla.TextBox( (15, 20*21, -15, 20), "Apply to layers:", sizeStyle='regular' )
		self.w.applyToLayers = vanilla.RadioGroup( (35, 20*22+10, -15, 20*2), ["Only master layers", "All the layers"], isVertical = True, sizeStyle='regular', callback=self.SavePreferences )

		# Run Button:
		self.w.runButton = vanilla.Button( (-240+15, -20-15, -15, -15), "Are you sure? START!", sizeStyle='regular', callback=self.StartFromScratchMain )
		self.w.setDefaultButton( self.w.runButton )

		# Load Settings:
		if not self.LoadPreferences():
			print "Note: 'Start-from-scratch' could not load preferences. Will resort to defaults"

		# Open window and focus on it:
		self.w.open()
		self.w.makeKey()

	def SavePreferences( self, sender ):
		try:
			Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanPaths"] = self.w.cleanPaths.get()
			Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanBackgrounds"] = self.w.cleanBackgrounds.get()
			Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanImages"] = self.w.cleanImages.get()
			Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanAnnotations"] = self.w.cleanAnnotations.get()
			Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanGuidelines"] = self.w.cleanGuidelines.get()
			Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanLabels"] = self.w.cleanLabels.get()
			Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanMetrics"] = self.w.cleanMetrics.get()
			Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanKerning"] = self.w.cleanKerning.get()
			Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanLayers"] = self.w.cleanLayers.get()
			Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanAnchors"] = self.w.cleanAnchors.get()

			Glyphs.defaults["com.pedroarilla.StartFromScratch.applyToGlyphs"] = self.w.applyToGlyphs.get()
			Glyphs.defaults["com.pedroarilla.StartFromScratch.applyToMasters"] = self.w.applyToMasters.get()
			Glyphs.defaults["com.pedroarilla.StartFromScratch.applyToLayers"] = self.w.applyToLayers.get()

			anyOptionOn = Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanPaths"] or Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanBackgrounds"] or Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanImages"] or Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanAnnotations"] or Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanGuidelines"] or Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanLabels"] or Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanMetrics"] or Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanKerning"] or Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanLayers"] or Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanAnchors"]
			self.w.runButton.enable(anyOptionOn)
		except:
			return False
		return True

	def LoadPreferences( self ):
		try:
			NSUserDefaults.standardUserDefaults().registerDefaults_(
				{
					"com.pedroarilla.StartFromScratch.cleanPaths": 0,
					"com.pedroarilla.StartFromScratch.cleanBackgrounds": 0,
					"com.pedroarilla.StartFromScratch.cleanImages": 0,
					"com.pedroarilla.StartFromScratch.cleanAnnotations": 0,
					"com.pedroarilla.StartFromScratch.cleanGuidelines": 0,
					"com.pedroarilla.StartFromScratch.cleanLabels": 0,
					"com.pedroarilla.StartFromScratch.cleanMetrics": 0,
					"com.pedroarilla.StartFromScratch.cleanKerning": 0,
					"com.pedroarilla.StartFromScratch.cleanLayers": 0,
					"com.pedroarilla.StartFromScratch.cleanAnchors": 0,
					"com.pedroarilla.StartFromScratch.applyToGlyphs": 0,
					"com.pedroarilla.StartFromScratch.applyToMasters": 0,
					"com.pedroarilla.StartFromScratch.applyToLayers": 0,
					"com.pedroarilla.StartFromScratch.applyToLayers": 0
				}
			)
			self.w.cleanPaths.set( Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanPaths"] )
			self.w.cleanBackgrounds.set( Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanBackgrounds"] )
			self.w.cleanImages.set( Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanImages"] )
			self.w.cleanAnnotations.set( Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanAnnotations"] )
			self.w.cleanGuidelines.set( Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanGuidelines"] )
			self.w.cleanLabels.set( Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanLabels"] )
			self.w.cleanMetrics.set( Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanMetrics"] )
			self.w.cleanKerning.set( Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanKerning"] )
			self.w.cleanLayers.set( Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanLayers"] )
			self.w.cleanAnchors.set( Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanAnchors"] )
			self.w.applyToGlyphs.set( Glyphs.defaults["com.pedroarilla.StartFromScratch.applyToGlyphs"] )
			self.w.applyToMasters.set( Glyphs.defaults["com.pedroarilla.StartFromScratch.applyToMasters"] )
			self.w.applyToLayers.set( Glyphs.defaults["com.pedroarilla.StartFromScratch.applyToLayers"] )
		except:
			return False
		return True

	def selectedGlyphs( self, thisFont, listOfGlyphs ):
		try:
			for glyph in thisFont.selectedLayers:
				listOfGlyphs.append(glyph.parent)
			return listOfGlyphs
		except:
			return False

	def allGlyphs( self, thisFont, listOfGlyphs ):
		try:
			listOfGlyphs = thisFont.glyphs
			return listOfGlyphs
		except:
			return False

	def activeMaster( self, listOfGlyphs, listOfMasters, thisFontMasterID ):
		try:
			for glyph in listOfGlyphs:
				for layer in glyph.layers:
					if layer.associatedMasterId == thisFontMasterID:
						listOfMasters.append(layer)
			return listOfMasters
		except:
			return False

	def allMasters( self, listOfGlyphs, listOfMasters ):
		try:
			for glyph in listOfGlyphs:
				for layer in glyph.layers:
					listOfMasters.append(layer)
			return listOfMasters
		except:
			return False

	def masterLayers( self, listOfMasters, listOfLayers ):
		try:
			for layer in listOfMasters:
				if layer.layerId == layer.associatedMasterId:
					listOfLayers.append(layer)
			return listOfLayers
		except:
			return False

	def cleanPaths( self, listOfLayers ):
		try:
			for layer in listOfLayers:
				layer.setPaths_( None )
				layer.setComponents_( None )
			return True
		except:
			return False

	def cleanBackgrounds( self, listOfLayers ):
		try:
			for layer in listOfLayers:
				layer.setBackground_( None )
			return True
		except:
			return False

	def cleanImages( self, listOfLayers ):
		try:
			for layer in listOfLayers:
				layer.setBackgroundImage_( None )
			return True
		except:
			return False

	def cleanAnnotations( self, listOfLayers ):
		try:
			for layer in listOfLayers:
				for annotation in layer.annotations:
					del(layer.annotations[0])
			return True
		except:
			return False

	def cleanGuidelines( self, thisFont, listOfLayers ):
		try:
			thisFont.selectedFontMaster.guideLines = []
			for layer in listOfLayers:
				layer.guideLines = []
			return True
		except:
			return False

	def cleanLabels( self, listOfGlyphs ):
		try:
			for glyph in listOfGlyphs:
				glyph.color = -1
			return True
		except:
			return False

	def cleanAnchors( self, listOfLayers ):
		try:
			for layer in listOfLayers:
				layer.setAnchors_( None )
			return True
		except:
			return False

	def cleanMetrics( self, listOfGlyphs ):
		try:
			for glyph in listOfGlyphs:
				glyph.setLeftMetricsKey_( None )
				glyph.setWidthMetricsKey_( None )
				glyph.setRightMetricsKey_( None )
				for layer in glyph.layers:
					layer.setLeftMetricsKey_( None )
					layer.setWidthMetricsKey_( None )
					layer.setRightMetricsKey_( None )
					layer.width = 600
					layer.LSB = 0
					layer.RSB = 0
			return True
		except:
			return False

	def cleanKerning( self, listOfGlyphs ):
		try:
			for glyph in listOfGlyphs:
				glyph.setLeftKerningGroup_( None )
				glyph.setRightKerningGroup_( None )
			return True
		except:
			return False

	def cleanLayers( self, listOfMasters ):
		try:
			for layer in listOfMasters:
				glyph = layer.parent
				if not layer.layerId == layer.associatedMasterId:
					del glyph.layers[layer.layerId]
			return True
		except:
			return False

	def StartFromScratchMain( self, sender ):
		try:
			Glyphs.clearLog()
			Glyphs.showMacroWindow()
			print "Start-from-scratch @ " + time.strftime("%H:%M:%S") + "\n"

			thisFont = Glyphs.font
			listOfGlyphs = []
			listOfMasters = []
			listOfLayers = []
			thisFont.disableUpdateInterface()

			# User selection:
			# Playground:
			if Glyphs.defaults["com.pedroarilla.StartFromScratch.applyToGlyphs"] == 0:
				print "\tGetting selected glyphs..."
				listOfGlyphs = self.selectedGlyphs( thisFont, listOfGlyphs )
			else:
				print "\tGetting all the glyphs in font..."
				listOfGlyphs = self.allGlyphs( thisFont, listOfGlyphs )
			if Glyphs.defaults["com.pedroarilla.StartFromScratch.applyToMasters"] == 0:
				print "\tSelecting active master..."
				thisFontMasterID = thisFont.selectedLayers[0].associatedFontMaster().id
				listOfMasters = self.activeMaster( listOfGlyphs, listOfMasters, thisFontMasterID )
			else:
				print "\tSelecting all the masters..."
				listOfMasters = self.allMasters( listOfGlyphs, listOfMasters )
			if Glyphs.defaults["com.pedroarilla.StartFromScratch.applyToLayers"] == 0:
				print "\tPicking master layers..."
				listOfLayers = self.masterLayers( listOfMasters, listOfLayers )
			else:
				print "\tPicking all the layers..."
				listOfLayers = listOfMasters

			# Playbook:
			if Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanAnchors"]:
				print "\tDeleting anchors..."
				self.cleanAnchors( listOfLayers )
			if Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanAnnotations"]:
				print "\tDeleting annotations..."
				self.cleanAnnotations( listOfLayers )
			if Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanBackgrounds"]:
				print "\tCleaning backgrounds..."
				self.cleanBackgrounds( listOfLayers )
			if Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanGuidelines"]:
				print "\tDeleting guidelines..."
				self.cleanGuidelines( thisFont, listOfLayers )
			if Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanImages"]:
				print "\tDeleting images..."
				self.cleanImages( listOfLayers )
			if Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanKerning"]:
				print "\tCleaning kerning groups..."
				self.cleanKerning( listOfGlyphs )
			if Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanLabels"]:
				print "\tCleaning labels..."
				self.cleanLabels( listOfGlyphs )
			if Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanMetrics"]:
				print "\tCleaning metric keys..."
				self.cleanMetrics( listOfGlyphs )
			if Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanLayers"]:
				print "\tDeleting non-master layers..."
				self.cleanLayers( listOfMasters )
			if Glyphs.defaults["com.pedroarilla.StartFromScratch.cleanPaths"]:
				print "\tDeleting paths and components..."
				self.cleanPaths( listOfLayers )

			thisFont.enableUpdateInterface()
			print "\nNow you can start from scratch! :)"

			if not self.SavePreferences( self ):
				print "Note: 'Start-from-scratch' could not write preferences."

			self.w.close() # delete if you want window to stay open

		except Exception, e:
			# brings macro window to front and reports error:
			Glyphs.clearLog()
			print "Start-from-scratch @ " + time.strftime("%H:%M:%S")
			Glyphs.showMacroWindow()
			print "Start-from-scratch Error: %s" % e
			import traceback
			print traceback.format_exc()

startFromScratch()
