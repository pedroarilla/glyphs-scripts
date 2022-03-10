#MenuTitle: KernSym
# -*- coding: utf-8 -*-
# by Pedro Arilla
# Source: https://www.dropbox.com/s/atjf1k6cz7jix4x/check-kerning.txt?dl=0
from __future__ import division, print_function, unicode_literals
__doc__="""
Opens a new tab and outputs a text with symbols to test kerning.
"""

import GlyphsApp, time
Glyphs.clearLog()
print("New tab @ " + time.strftime("%H:%M:%S"))

text = """
WOW.” ,’ ,” .’ ?” ?’ !” !’
.1.2.3.4.5.6.7.8.9.0.
,1,2,3,4,5,6,7,8,9,0,
-1-2-3-4-5-6-7-8-9-0-
–1–2–3–4–5–6–7–8–9–0–
-a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z-
-A-B-C-D-E-F-G-H-I-J-K-L-M-N-O-P-Q-R-S-T-U-V-W-X-Y-Z-
ÐaÐbÐcÐdÐeÐfÐgÐhÐiÐjÐkÐlÐmÐnÐoÐpÐqÐrÐsÐtÐuÐvÐwÐxÐyÐzÐ
ÐAÐBÐCÐDÐEÐFÐGÐHÐIÐJÐKÐLÐMÐNÐOÐPÐQÐRÐSÐTÐUÐVÐWÐXÐYÐZÐ
ÑaÑbÑcÑdÑeÑfÑgÑhÑiÑjÑkÑlÑmÑnÑoÑpÑqÑrÑsÑtÑuÑvÑwÑxÑyÑzÑ
ÑAÑBÑCÑDÑEÑFÑGÑHÑIÑJÑKÑLÑMÑNÑOÑPÑQÑRÑSÑTÑUÑVÑWÑXÑYÑZÑ
—a—b—c—d—e—f—g—h—i—j—k—l—m—n—o—p—q—r—s—t—u—v—w—x—y—z—
–a–b–c–d–e–f–g–h–i–j–k–l–m–n–o–p–q–r–s–t–u–v–w–x–y–z–
–A–B–C–D–E–F–G–H–I–J–K–L–M–N–O–P–Q–R–S–T–U–V–W–X–Y–Z–
—A—B—C—D—E—F—G—H—I—J—K—L—M—N—O—P—Q—R—S—T—U—V—W—X—Y—Z—
.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z.
,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,
.A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z.
,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,
a; b; c; d; e; f; g; h; i; j; k; l; m; n; o; p; q; r; s; t; u; v; w; x; y; z;
a: b: c: d: e: f: g: h: i: j: k: l: m: n: o: p: q: r: s: t: u: v: w: x: y: z:
A; B; C; D; E; F; G; H; I; J; K; L; M; N; O; P; Q; R; S; T; U; V; W; X; Y; Z;
A: B: C: D: E: F: G: H: I: J: K: L: M: N: O: P: Q: R: S: T: U: V: W: X: Y: Z:
//a//b//c//d//e//f//g//h//i//j//k//l//m//n//o//p//q//r//s//t//u//v//w//y//z//
//A//B//C//D//E//F//G//H//I//J//K//L//M//N//O//P//Q//R//S//T//U//V//W//X//Y//Z//
A?B?C?D?E?F?G?H?I?J?K?L?M?N?O?P?Q?R?S?T?U?V?W?X?Y?Z?
a?b?c?d?e?f?g?h?i?j?k?l?m?n?o?p?q?r?s?t?u?v?w?x?y?z?
a! b! c! d! e! f! g! h! i! j! k! l! m! n! o! p! q! r! s! t! u! v! w! x! y! z!
A! B! C! D! E! F! G! H! I! J! K! L! M! N! O! P! Q! R! S! T! U! V! W! X! Y! Z!
“A” “B” “C” “D” “E” “F” “G” “H” “I” “J” “K” “L” “M” “N” “O” “P” “Q” “R” “S” “T” “U” “V” “W” “X” “Y” “Z”
“a” “b” “c” “d” “e” “f” “g” “h” “i” “j” “k” “l” “m” “n” “o” “p” “q” “r” “s” “t” “u” “v” “w” “x” “y” “z”
‘A’ ‘B’ ‘C’ ‘D’ ‘E’ ‘F’ ‘G’ ‘H’ ‘I’ ‘J’ ‘K’ ‘L’ ‘M’ ‘N’ ‘O’ ‘P’ ‘Q’ ‘R’ ‘S’ ‘T’ ‘U’ ‘V’ ‘W’ ‘X’ ‘Y’ ‘Z’
‘a’ ‘b’ ‘c’ ‘d’ ‘e’ ‘f’ ‘g’ ‘h’ ‘i’ ‘j’ ‘k’ ‘l’ ‘m’ ‘n’ ‘o’ ‘p’ ‘q’ ‘r’ ‘s’ ‘t’ ‘u’ ‘v’ ‘w’ ‘x’ ‘y’ ‘z’
’a’b’c’d’e’f’g’h’i’j’k’l’m’n’o’p’q’r’s’t’u’v’w’x’y’z’
’A’B’C’D’E’F’G’H’I’J’K’L’M’N’O’P’Q’R’S’T’U’V’W’X’Y’Z’
$12 $23 $34 $45 $56 $67 $78 $89 $90 $01
€12 €23 €34 €45 €56 €67 €78 €89 €90 €01
£12 £23 £34 £45 £56 £67 £78 £89 £90 £01
¥12 ¥23 ¥34 ¥45 ¥56 ¥67 ¥78 ¥89 ¥90 ¥01
12¢ 23¢ 34¢ 45¢ 56¢ 67¢ 78¢ 89¢ 90¢ 01¢
(a)(b)(c)(d)(e)(f)(g)(h)(i)(j)(k)(l)(m)(n)(o)(p)(q)(r)(s)(t)(u)(v)(w)(x)(y)(z)
(A)(B)(C)(D)(E)(F)(G)(H)(I)(J)(K)(L)(M)(N)(O)(P)(Q)(R)(S)(T)(U)(V)(W)(X)(Y)(Z)
{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}{m}{n}{o}{p}{q}{r}{s}{t}{u}{v}{w}{x}{y}{z}
{A}{B}{C}{D}{E}{F}{G}{H}{I}{J}{K}{L}{M}{N}{O}{P}{Q}{R}{S}{T}{U}{V}{W}{X}{Y}{Z}
[a][b][c][d][e][f][g][h][i][j][k][l][m][n][o][p][q][r][s][t][u][v][w][x][y][z]
[A][B][C][D][E][F][G][H][I][J][K][L][M][N][O][P][Q][R][S][T][U][V][W][X][Y][Z]
"""

Font.newTab(text)

print("Tab opened.")
