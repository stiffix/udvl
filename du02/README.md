Domáca úloha 2
==============

Domácu úlohu odovzdávajte do Štvrtku 17.4. 9:55 (t.j. najneskôr
na začiatku prednášky).

Úlohu odovzdávajte buď fyzicky na papier formátu A4 (čitateľne označenom a
podpísanom) na prednáške alebo na cvičeniach, alebo elektronicky vo formáte PDF
(ako súbor `du02.pdf`) alebo ako obyčajný textový súbor (`du02.txt`, `du02.md`)
do vetvy `du02`.  Môžete odovzdať aj oskenované/odfotené
papierové verzie ako súbor `du02.jpg` alebo `du02.png`, ak sú dostatočne čitateľné
(dostatočné rozlíšenie, kontrast, v oskenovanej verzii sa škaredé písmo trochu
ťažšie lúšti,...). Nezabudnite vyrobiť pull request.

Bohužiaľ cez webové rozhranie sa na github dajú súbory len priamo písať alebo
copy-paste-ovať, binárne súbory treba nahrať pomocou
GIT-u ([msysgit](http://msysgit.github.io/) alebo čistý [git](http://git-scm.com/downloads))
alebo [github programu pre windows](http://windows.github.com/)
respektíve pre [Mac](http://mac.github.com/).

Github pre windows/mac je vcelku jednoduchý: stačí nainštalovať, zadať meno a heslo,
naklonovať svoj repozitár, prepnúť správnu vetvu, nahrať do správnych adresárov súbory,
commit-núť a nahrať na server (v tomto programe to volajú "sync/synchronize branch").
Samozrejme potom treba ešte (cez webová rozhranie) vyrobiť pull request.

## 2.1 (1b)

Rozhodnite a **dokážte** či sú nasledovné formuly splniteľné:

a) ((&not;p&rarr;r)&rarr;(r&rarr;&not;p))

b) ((a&rarr;((b&or;c)&rarr;d))&and;&not;((a&rarr;(b&or;c))&rarr;(a&rarr;d)))


## 2.2 (2b)
Bez práce nie sú koláče. Ak niekto nemá ani koláče, ani chleba, tak bude
hladný. Na chlieb treba múku. Dokážte, že ak niekto nemá múku ale je najedený,
tak pracoval. (Jednotlivé tvrdenia sformalizujte pomocou výrokovologických
premenných **práca**, **koláče**, **chlieb**, **múka** a **hlad**.)


## 2.3 (1b)

Rozhodnite a **dokážte**, či je nasledovná formula tautológia

( (a&or;(&not;b&and;(c&and;d))) &rarr;
( ((b&or;&not;(c&and;e)) &rarr; (a&or;e)) &and; ((b&or;&not;d) &rarr; a) )


## Príklad veľmi jednoduchého tabla
<table style="text-align: center;">
  <tr> <td colspan="2">(1) F (&not;(a&and;b) &rarr; (&not;a&or;&not;b))</td> </tr>
  <tr> <td colspan="2">(2) T &not;(a&and;b) [1]</td> </tr>
  <tr> <td colspan="2">(3) F (&not;a&or;&not;b) [1]</td> </tr>
  <tr> <td colspan="2" style="border-bottom: 1px solid black;">(4) F (a&and;b) [2]</td> </tr>
  <tr> <td style="border-right: 1px solid black;"> (5) F a          </td> <td> (8) F  b [4] </td></tr>
  <tr> <td style="border-right: 1px solid black;"> (6) F &not;a [3] </td> <td> (9) F &not;b [3] </td></tr>
  <tr> <td style="border-right: 1px solid black;"> (7) T a [6]      </td> <td> (10) T b  [9] </td></tr>
  <tr> <td style="border-right: 1px solid black;"> * [5 a 7]        </td> <td> * [8 a 10]</td></tr>
</table>
