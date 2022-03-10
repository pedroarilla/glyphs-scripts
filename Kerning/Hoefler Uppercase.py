#MenuTitle: Hoefler Uppercase
# -*- coding: utf-8 -*-
# by Pedro Arilla
# Source: https://www.typography.com/blog/text-for-proofing-fonts
from __future__ import division, print_function, unicode_literals
__doc__="""
Opens a new tab and outputs a text by Hoefler&Co. to test kerning.
"""

import GlyphsApp, time
Glyphs.clearLog()
print("New tab @ " + time.strftime("%H:%M:%S"))

text = """
ABIDE ACORN OF THE HABIT DACRON FOR THE BUDDHA GOUDA QUAALUDE. BENCH BOGUS OF THE SCRIBE ROBOT FOR THE APLOMB JACOB RIBBON. CENSUS CORAL OF THE SPICED JOCOSE FOR THE BASIC HAVOC SOCCER. DEMURE DOCILE OF THE TIDBIT LODGER FOR THE CUSPID PERIOD BIDDER. EBBING ECHOING OF THE BUSHED DECAL FOR THE APACHE ANODE NEEDS. FEEDER FOCUS OF THE LIFER BEDFORD FOR THE SERIF PROOF BUFFER. GENDER GOSPEL OF THE PIGEON DOGCART FOR THE SPRIG QUAHOG DIGGER. HERALD HONORS OF THE DIHEDRAL MADHOUSE FOR THE PENH RIYADH BATHHOUSE. IBSEN ICEMAN OF THE APHID NORDIC FOR THE SUSHI SAUDI SHIITE. JENNIES JOGGER OF THE TIJERA ADJOURN FOR THE ORANJ KOWBOJ HAJJIS. KEEPER KOSHER OF THE SHRIKE BOOKCASE FOR THE SHEIK LOGBOOK CHUKKAS. LENDER LOCKER OF THE CHILD GIGOLO FOR THE UNCOIL GAMBOL ENROLLED. MENACE MCCOY OF THE NIMBLE TOMCAT FOR THE DENIM RANDOM SUMMON. NEBULA NOSHED OF THE INBRED BRONCO FOR THE COUSIN CARBON KENNEL. OBSESS OCEAN OF THE PHOBIC DOCKSIDE FOR THE GAUCHO LIBIDO HOODED. PENNIES PODIUM OF THE SNIPER OPCODE FOR THE SCRIP BISHOP HOPPER. QUANTA QOPHS OF THE INQUEST OQOS FOR THE CINQ COQ SUQQU. REDUCE ROGUE OF THE GIRDLE ORCHID FOR THE MEMOIR SENSOR SORREL. SENIOR SCONCE OF THE DISBAR GODSON FOR THE HUBRIS AMENDS LESSEN. TENDON TORQUE OF THE UNITED SCOTCH FOR THE NOUGHT FORGOT BITTERS. UNDER UGLINESS OF THE RHUBARB SEDUCE FOR THE MANCHU HINDU CONTINUUM. VERSED VOUCH OF THE DIVER OVOID FOR THE TELAVIV KARPOV FLIVVER. WENCH WORKER OF THE UNWED SNOWCAP FOR THE ANDREW ESCROW GLOWWORM. XENON XOCHITL OF THE MIXED BOXCAR FOR THE SUFFIX ICEBOX EXXON. YEOMAN YONDER OF THE HYBRID ARROYO FOR THE DINGHY BRANDY SAYYID. ZEBRA ZOMBIE OF THE PRIZED OZONE FOR THE FRANZ ARROZ BUZZING.
"""

Font.newTab(text)

print("Tab opened.")