#MenuTitle: Vertical metrics checker
# -*- coding: utf-8 -*-
# by Pedro Arilla
__doc__="""
Checks rational across vertical metrics (win, typo, and hhea values) and consistency across masters.
"""

import GlyphsApp
import time
Glyphs.clearLog()
Glyphs.showMacroWindow()
print "Vertical metrics checker @ " + time.strftime("%H:%M:%S")

thisFont = Glyphs.font
yep = "\U00002705"
nope = "\U0000274C"
metricKeys = {"typoAscender" : [], "typoDescender" : [], "typoLineGap" : [], "hheaAscender" : [], "hheaDescender" : [], "hheaLineGap" : [], "winDescent" : [], "winAscent" : []}

try:

    # 1st test
    print "\t# 1st test: typoAscender + abs(typoDescender) = UPM"
    for master in thisFont.masters:
        if master.customParameters["typoAscender"] + abs(master.customParameters["typoDescender"]) == thisFont.upm:
            print "\t\t" + yep.decode('unicode-escape') + " " + master.name
        else:
            print "\t\t" + nope.decode('unicode-escape') + " " + master.name

    # 2nd test
    print "\t# 2nd test: winDescent is a positive value"
    for master in thisFont.masters:
        if master.customParameters["winDescent"] > 0:
            print "\t\t" + yep.decode('unicode-escape') + " " + master.name
        else:
            print "\t\t" + nope.decode('unicode-escape') + " " + master.name

    # 3rd test
    print "\t# 3rd test: hheaAscender = winAscent"
    for master in thisFont.masters:
        if master.customParameters["winAscent"] == master.customParameters["hheaAscender"]:
            print "\t\t" + yep.decode('unicode-escape') + " " + master.name
        else:
            print "\t\t" + nope.decode('unicode-escape') + " " + master.name

    # 4th test
    print "\t# 4th test: abs(hheaDescender) = winDescent"
    for master in thisFont.masters:
        if master.customParameters["winDescent"] == abs(master.customParameters["hheaDescender"]):
            print "\t\t" + yep.decode('unicode-escape') + " " + master.name
        else:
            print "\t\t" + nope.decode('unicode-escape') + " " + master.name

    # 5h test
    print "\t# 5th test: typoLineGap = hheaLineGap = 0"
    for master in thisFont.masters:
        if master.customParameters["typoLineGap"] == master.customParameters["hheaLineGap"] == 0:
            print "\t\t" + yep.decode('unicode-escape') + " " + master.name
        else:
            print "\t\t" + nope.decode('unicode-escape') + " " + master.name

    # 6th test
    print "\t# 6th test: consistency across masters"
    for master in thisFont.masters:
        for key, list in metricKeys.iteritems():
            list.append([master, master.customParameters[key]])
    for key, list in metricKeys.iteritems():
        compare = []
        for sublist in list:
            compare.append(sublist[1])
        if compare[1:] == compare[:-1]:
            print "\t\t" + yep.decode('unicode-escape') + " " + key
        else:
            print "\t\t" + nope.decode('unicode-escape') + " " + key
            for pair in list:
                print "\t\t\t" + str(pair[1]) + " @ " + pair[0].name

    print "Vertical metrics checked."
except:
    print "Error: There is a value missing."
