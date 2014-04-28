Úvod do výpočtovej logiky
=========================

Stránka predmetu je http://dai.fmph.uniba.sk/~siska/udvl/.

Oznamy
------

* **28.4.** V pondelok 5.5. nebude normálne cvičenie (štvrtkové odpadne),
    ale budú "konzultácie", na ktoré môžete prísť prediskutovať akékoľvek
    otázky ohľadom cvík, domácich úloh alebo predmetu.
* **28.4.** V programe na projektore na štvrtkových cvikách boli 2 chyby:
    * V metóde `Clause.findNewWatch` bolo priamo priradenie
      `self.watched[wi] = ...` namiesto použitia metódy `setWatch(wi, ...)`
      (hneď dvakrát ;). Toto spôsobuje, že sa korektne neudržiava pre každý
      literál zoznam kláuz, kde je označený.
    * V metóde `Solver.setLiteral` je potrebné ešte na začiatku
      skontrolovať, či ten literál už nie je nastavený (nespraviť nič, ak je
      už nastavený správne, vrátiť `False`, ak je už nastavený opačne, aj
      keď tento prípad by nastať nemal, lebo to by sa zistilo počas
      vyberania nového označeného literálu). Toto môže nastať, ak počas
      unitPropagte viacero klauz nastaví daný literál
      (napríklad `1 0 -1 2 0 -1 2 0`).
* **13.4.** Termín 2. domácej úlohy bol posunutý na 24.4. (17.4. je voľno).
* **13.4.** V testovači pre cv08 bola drobná chybička, ktorá zle testovala
    úplnosť vetvy a nesprávne produkovala chyby, ak `getType` pre `Variable`
    vracala `None` (riešenia, ktoré pre `Variable` dávali typ `ALPHA` boli testované
    OK). Nahraná je už opravená verzia testovača.
* **28.3.** Prehľad o všetkých bodoch z cvičení a úloh si môžete pozrieť v súbore
    `report.md` vo vetve `report` (samozrejme nájdete ich aj v príslušných pull
    requestoch). Priame url je (nezabudnite nahradiť LOGIN za vaše
    prihlasovacie meno):

       https://github.com/FMFI-UK-1-AIN-411-2014/LOGIN/blob/report/report.md
* **27.3.** Midterm bude vo štvrtok 10.4. o 18:10 (po cvičeniach) v posluchárni B.
* **21.3.** du01: pridaná možnosť odovzdávať .txt a poznámka o tom ako nahrávať binárne súbory

Cvičenia
--------
* Pon 12:20 H6
* Štv 16:30 H6

Zadania:

* [Cvičenie 1](cv01) (do Pondelka 3.3. 23:59:59)
* [Cvičenie 2](cv02) (do Nedele 9.3. 23:59:59)
* [Cvičenie 3](cv03) (do Nedele 16.3.  23:59:59)
* [Cvičenie 4](cv04) (do Nedele 23.3.  23:59:59)
* [Cvičenie 5](cv05) (do Nedele 30.3.  23:59:59)
* [Cvičenie 6](cv06) (do Nedele 6.4.  23:59:59)
* [Cvičenie 7](cv07) (do Nedele 13.4.  23:59:59)
* [Cvičenie 8](cv08) (do Nedele 20.4.  23:59:59)
* [Cvičenie 9](cv09) (do Nedele 11.5.  23:59:59)

Bonusy:

* [Bonus 1](bonus01) (do Nedele 23.3.  23:59:59)

Domáce úlohy
------------

* [DU 1](du01) (do Štvrtku 27.3. 9:55)
* [DU 2](du02) (do Štvrtku 17.4. 9:55)

[Inštrukcie na odovzdávanie riešení](odovzdavanie.md)

Za účelom odovzdávania cvičení získate prístup k súkromnému repozitáru na GitHub-e.
Používaním tohoto repozitára (t.j. nahrávaním súbrov, napríklad vašich riešení) prejavujte
svoj súhlas s nasledovnými podmienkami:
- Do repozitára budete nahrávať iba materiály súvisiace s predmetom.
- Do repozitára budete nahrávať iba materiály, ktoré máte právo zverejniť
  (vzhľadom na autorské práva, iné zákony a pravidlá).
Tieto podmienky sú súčasťou podmienok na absolvovanie tohoto predmetu.
