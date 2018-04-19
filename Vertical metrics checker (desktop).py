#MenuTitle: Vertical metrics checker (desktop)
# -*- coding: utf-8 -*-
# by Pedro Arilla
__doc__="""
Checks consistency across vertical metrics (win, typo, and hhea values) and across masters.
"""

import GlyphsApp
import time
Glyphs.clearLog()
Glyphs.showMacroWindow()
print "Vertical metrics checker (desktop) @ " + time.strftime("%H:%M:%S")

thisFont = Glyphs.font
yep = "\U00002705"
nope = "\U0000274C"
metricKeys = {"typoAscender" : [], "typoDescender" : [], "typoLineGap" : [], "hheaAscender" : [], "hheaDescender" : [], "hheaLineGap" : [], "winDescent" : [], "winAscent" : []}

try:
    total = thisFont.masters[0].customParameters["winAscent"] + thisFont.masters[0].customParameters["winDescent"]
    print "\tCrop area 1st master: " + str(total)

    # 1st test
    print "\t# 1st test: typoAscender + typoDescender = 1000"
    for master in thisFont.masters:
        if abs(master.customParameters["typoAscender"]) + abs(master.customParameters["typoDescender"]) == 1000:
            print "\t\t" + yep.decode('unicode-escape') + " " + master.name
        else:
            print "\t\t" + nope.decode('unicode-escape') + " " + master.name

    # 2nd test
    print "\t# 2nd test: sum[typo_values] = sum[win_values]"
    for master in thisFont.masters:
        if abs(master.customParameters["typoAscender"]) + abs(master.customParameters["typoDescender"]) + abs(master.customParameters["typoLineGap"]) == total:
            print "\t\t" + yep.decode('unicode-escape') + " " + master.name
        else:
            print "\t\t" + nope.decode('unicode-escape') + " " + master.name

    # 3rd test
    print "\t# 3rd test: hhea_values = typo_values"
    for master in thisFont.masters:
        if master.customParameters["typoAscender"] == master.customParameters["hheaAscender"]:
            print "\t\t" + yep.decode('unicode-escape') + " " + master.name + "/Ascender"
        else:
            print "\t\t" + nope.decode('unicode-escape') + " " + master.name + "/Ascender"
        if master.customParameters["typoDescender"] == master.customParameters["hheaDescender"]:
            print "\t\t" + yep.decode('unicode-escape') + " " + master.name + "/Descender"
        else:
            print "\t\t" + nope.decode('unicode-escape') + " " + master.name + "/Descender"
        if master.customParameters["typoLineGap"] == master.customParameters["hheaLineGap"]:
            print "\t\t" + yep.decode('unicode-escape') + " " + master.name + "/LineGap"
        else:
            print "\t\t" + nope.decode('unicode-escape') + " " + master.name + "/LineGap"

    # 4th test
    print "\t# 4th test: consistency across masters"
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
