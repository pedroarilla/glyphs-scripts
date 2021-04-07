#MenuTitle: Vertical metrics reporter
# -*- coding: utf-8 -*-
# by Pedro Arilla
from __future__ import division, print_function, unicode_literals
__doc__="""
Reports if vertical metrics in all the masters in all open files are equal.
"""

import GlyphsApp, time
Glyphs.clearLog()
Glyphs.showMacroWindow()
print("Vertical metrics reporter @ " + time.strftime("%H:%M:%S"))

metricKeys = {"typoAscender" : [], "typoDescender" : [], "typoLineGap" : [], "hheaAscender" : [], "hheaDescender" : [], "hheaLineGap" : [], "winDescent" : [], "winAscent" : []}

for i in range(0,len(Glyphs.fonts)):
    for master in Glyphs.fonts[i].masters:
        for key, list in metricKeys.iteritems():
            list.append([Glyphs.fonts[i].parent.displayName(), master, master.customParameters[key]])

for key, list in metricKeys.iteritems():
    compare = []
    for sublist in list:
        compare.append(sublist[2])
    if compare[1:] == compare[:-1]:
        print("\t✅ " + key)
    else:
        print("\t❌ " + key)
        for pair in list:
            print("\t\t" + str(pair[2]) + " @ " + pair[0] + "/" + pair[1].name)

print("Vertical metrics reported.")
