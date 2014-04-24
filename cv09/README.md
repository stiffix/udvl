Cvičenie 9
==========

**Riešenie odovzdávajte podľa
[pokynov na konci tohoto zadania](#technické-detaily-riešenia)
do Nedele 11.5.  23:59:59.**

Súbory potrebné pre toto cvičenie si môžete stiahnúť ako jeden zip
[`cv09.zip`](https://github.com/FMFI-UK-1-AIN-411-2014/udvl/archive/cv09.zip).

SAT solver (4b)
----------

Naprogramujte SAT solver, ktorý zisťuje, či je vstupná formula (v konjunktívnej
normálnej forme) splniteľná.

Na prednáške bola základná kostra DPLL metódy, ktorej hlavnou ideou je
propagácia klauz s iba jednou premennou (unit clause).  Tá ale hovorí o veciach
ako *vymazávanie literálov* z klauz a *vymazávanie klauz*, čo sú veci, ktoré nie
je také ľahké efektívne (či už časovo alebo pamäťovo) implementovať, hlavne ak
počas backtrackovania treba zmazané literály resp.  klauzy správne naspäť
obnovovať.

Ukážeme si preto jednoduchú modifikáciu DPLL metódy, ktorá výrazne zjednodušuje
"menežment" literálov, klauz a dátových štruktúr.

## Watched literals

Základným problémom pri DPLL metóde je vedieť povedať, či už klauza obsahuje
nejaký literál ohodnotený `true` (a teda je už splnená), ak nie, tak či obsahuje
práve jeden neohodnotený literál (unit clause), alebo či už sú všetky literály
`false` (nesplnená klauza: treba backtrackovať).

Namiesto mazania / obnovovania literálov a klauz si pre každú klauzu si označíme
/ budeme pamätať dva literály z nej, pričom budem požadovať aby každý z nich
- buď ešte nemal priradenú hodnotu,
- alebo mal priradenú hodnotu `true`.

Ak nejaký literál počas prehľadávania nastavíme na `true`, tak očividne nemusíme
nič meniť. Ak ho nastavíme na `false` (lebo sme napríklad jeho negáciu nastavili
na `true`) tak pre každú klauzu, v ktorej je označený, musíme nájsť nový
literál, ktorý spĺňa horeuvedené podmienky. Môžu nastať nasledovné možností:
- našli sme iný literál, ktorý je buď nenastavený, alebo je `true`, odteraz
  bude označený ten,
- nenašli sme už literál, ktorý by spĺňal naše podmienky (všetky ostatné sú
 `false`):
    - ak druhý označený literál bol `true`, tak to nevadí (klauza je aj tak splnená),
    - ale ak bol druhý literál nenastavený, tak nám práve vznikla unit clause, a mali by sme ho
      nastaviť na `true`.
    - podľa toho, ako presne implementujeme propagáciu, sa nám môže stať, že sa
      dostaneme do momentu, že aj druhý označený literál sa práve stal `false`,
      v tom prípade sme práve našli nesplnenú klauzu a musíme backtracovať.

Bonus navyše: ak backtrackujeme (meníme nejaký true alebo false literál naspäť
na nenastavený), tak nemusíme vôbec nič robiť (s označenými literálmi v klauzách;
samotný literál/premennú samozrejme musíme korektne "odnastaviť").


TODO pseudokod

## Technické detaily riešenia

Riešenie odovzdajte do vetvy `cv09` v adresári `cv09`.
Odovzdávajte (modifikujte) súbor `satsolver.py` resp `satsolver.cpp` / `SatSolver.java`.
Program [`cv09test.py`](cv09test.py) otestuje váš solver na rôznych vstupoch
(z adresara testData). Testovač by mal automaticky detekovať Python / C++ / Java
riešenia pritomne v adresári.

Vaším riešením má byť konzolový program (žiadne gui), ktorý dostane dva
argumenty: meno vstupné a výstupného súboru. Vstupný súbor bude v DIMACS
formáte s korektnou hlavičkou (môže obsahovať komentáre).

Do výstupného subóru váš program zapíše na prvý riadok buď `SAT` alebo `UNSAT`,
podľa toho, či je formula splniteľná. Ak je formula splniteľná, tak na druhý
riadok zapíše model (spĺňajúce ohodnotenie): medzerami oddelené čísla s
absolutnými hodnotami 1, 2, ... až najväčšia premenná. Kladné číslo znamená, že
premenná je nastavená na true a záporne, že je nastavená na false.
V predpripravenom `satsolver.py` už je implementované korektné načítavanie a zápis riešenia.

Za korektný beh programu sa považuje iba keď váš program skončí s návratovou hodnotou 0,
nenulová hodnota sa považuje za chybu (Runtime Error). Toto je dôležite hlavne v C++
(`return 0;` na konci `main`), ak Python korektne skončí, tak by mal vrátiť 0.

### C++
Odovzdávajte program `satsolver.cpp`, ktorý musí byť skompilovateľný príkazom
`g++ -Wall --std=c++11 -o satsolver *.cpp`.

###Java:
Odovzdávajte program `SatSolver.java`, ktorý implementuje triedu `SatSolver` s
main metódou. Kód musí byť skompilovateľný príkazom
`javac SatSolver.java`.

Odovzdávanie riešení v iných jazykoch konzultujte s cvičiacimi.
