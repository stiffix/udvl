Domáca úloha 3
==============

Domácu úlohu odovzdávajte elektronicky do Nedele 25.5. 23:59:59, fyzicky
najneskôr na cvičeniach vo štvrtok 22.5.

Úlohu odovzdávajte buď fyzicky na papier formátu A4 (čitateľne označenom a
podpísanom) na prednáške alebo na cvičeniach, alebo elektronicky vo formáte PDF
(ako súbor `du03.pdf`) alebo ako obyčajný textový súbor (`du03.txt`, `du03.md`)
do vetvy `du03`.  Môžete odovzdať aj oskenované/odfotené
papierové verzie ako súbor `du03.jpg` alebo `du03.png`, ak sú dostatočne čitateľné
(dostatočné rozlíšenie, kontrast, v oskenovanej verzii sa škaredé písmo trochu
ťažšie lúšti,...). Nezabudnite vyrobiť pull request.

## 3.1 (2b)

Zapíšte v prvorádovej logike nasledovné tvrdenia (ak sú v zátvorke uvedené konkrétne
predikáty, použitie tie):

1.  Nie každý, kto sa ti zalieča, je tvojím priateľom.
    (`zaliecasa(kto, komu)`, `priatel(kto, koho)`)
1.  Kto klame, ten kradne.
1. "[Valar morghulis](http://awoiaf.westeros.org/index.php/Valar_morghulis)".
1. "[You Know Nothing, Jon Snow](http://knowyourmeme.com/memes/you-know-nothing-jon-snow)".
1.  Kto nič nerobí, nič nepokazí.
    (`clovek(x)`, `cinnost(c)`,` robi(clovek, cinnost)`, `pokazi(clovek, cinnost)`)
1.  Niet na svete nikoho, kto by bol vždy šťastný. (`stastny(kto, kedy)`)
1.  "[All your base are belong to us](http://en.wikipedia.org/wiki/All_your_base_are_belong_to_us)"
    resp. všetky základne, ktoré patrili kapitánovi, teraz patria CATS.
    (`captain(x)`, `CATS(x)`, `base(x)`, `time(t)`, `before(t_before,t_after)`, `owns(time, base, who)`,
       `now(time))`.

1.  Lež večná meno toho nech ovenčí sláva,<br/>
    kto seba v obeť svätú za svoj národ dáva.

<!--
        Ale vieš ty to, srdce neznané, 
        že komu panej srdce je dané, 
        ten mňa si tiež má dobývať. 

        Možno mi tvojich úst sa odrieknuť, 
        možno mi ruky nedostať, 
        možno mi v diaľky žiaľne utieknuť, 
        možno mi nemilým ostať, 
        možno mi ústam smädom umierať, 
        možno mi žialiť v samote, 
        možno mi život v púšťach zavierať, 
        možno mi nežiť v živote, 
        možno mi seba samého zhubiť: - 
        nemožno mi ťa neľúbiť! - 
-->


## 3.2 (2b)
Sformalizujte v prvorádovej logike a dokážte:

Každý študent fakulty študuje matematiku, fyziku, alebo informatiku.
Študenti matematiky a fyziky sa učia programovať v C++ (majú zapísaný / navštevujú predmet C++),
študenti informatiky v pythone a jave.
Každý študent sa učí aspoň jeden z týchto jazykov, žiadny sa však neučí všetky.
Marienka sa učí programovať v C++.
Keďže sa Jankovi Marienka páči, tak si
zapísal aj všetky predmety, na ktoré Marienka chodí.
Aj napriek tomu, že má teraz Janko predmetov veľa, existuje aj študent,
ktorý s ním na žiadnu prednášku nechodí.
Dokážte, že existuje aspoň nejaký študent informatiky.

Poznámka: To, kto aký odbor študuje, je asi najlepšie reprezentovať
pomocou troch predikátov (napr. <em><b>i</b></em>nformatik(x),
<em><b>m</b></em>atik(x), <em><b>f</b></em>yzik(x)).


## 3.3 (1b)

Rozhodnite a **dokážte**, či sú nasledovné formuly platné.

1. (∀x(P(f(x)) → Q(x)) → (∃y(P(f(y))∨Q(y)) → (∃zQ(z) ∨ ∃zQ(g(z)))))
1. (∀x(P(x) → Q(g(x))) → ((∃yP(f(y)) ∨ ∃yQ(y)) → ∃z(Q(z) ∨ Q(g(z)))))



