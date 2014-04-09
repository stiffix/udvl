Cvičenie 8
==========

**Riešenie odovzdávajte podľa
[pokynov na konci tohoto zadania](#technické-detaily-riešenia)
do Nedele 20.4.  23:59:59.**

Súbory potrebné pre toto cvičenie si môžete stiahnúť ako jeden zip
[`cv08.zip`](https://github.com/FMFI-UK-1-AIN-411-2014/udvl/archive/cv08.zip).

Tablo (4b)
------------------

Implementujte tablový algoritmus.

Vaše riešenie sa má skladať z dvoch častí:

- do tried na reprezentáciu formúl z cvičenia 3 doimplementujte
  metódy `signedSubf` a `getType`, ktoré reprezentujú informácie o
  tablových pravidlách pre jednotlivé typy formúl
- implementujte triedu TableauBuild obsahujúcu metódu build,
  ktorá dostane zoznam označených formúl a vytvorí pre ne uzavreté
  alebo úplné tablo

Označené formuly reprezentujeme ako dvojice `(sign, formula)`, kde
`sign` je buď `True` (značka `T`) alebo `False` (značka `F`).

Metóda `getType(sign)` vráti akého typu (&alpha; alebo &beta;) by dotyčná
formula bola, ak by bola označená značkou `sign` (negácia a premenná sú vždy
typu &alpha;).

Metóda `signedSubf` vráti "podformuly" označenej formuly,
tj &alpha;<sub>1</sub> a &alpha;<sub>2</sub> ak by bola typu &alpha;
a &beta;<sub>1</sub> a &beta;<sub>2</sub> ak by bola typu &beta;.

Pamätajte, že konjukcia a disjunkcia môžu mať viacero podformúl, takže
tablové pravidlá v skutočnosti vyzerajú nasledovne:

```
        F A1∧A2∧A3∧...∧An
---------------------------------
 F A1 | F A2 | F A3 | ... | F An


 T A1∧A2∧A3∧...∧An
-------------------
       T A1
       T A2
       T A3
       ...
       T An
```


## Technické detaily riešenia

Riešenie odovzdajte do vetvy `cv08` v adresári `cv08`.  Odovzdávajte
(modifikujte) súbory `formula.py` a `builder.py`.  Program
[`cv08test.py`](cv08test.py) musí korektne zbehnúť s vašou knižnicou.

Odovzdávanie riešení v iných jazykoch konzultujte s cvičiacimi.
