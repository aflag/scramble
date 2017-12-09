Scramble
========

Have you ever wondered what is the most unintelligible anagram from your
favourite word? Wonder no more! You can use this library's best_scramble to
find that out (if you are not afraid of a little O(n!) computation, that is).
Alternatively, you can use the scramble function, if you just want a good enough
algorithm.

What makes a anagram more or less similar to the original word?
---------------------------------------------------------------

A word is made of syllables and those syllables are made of letters. In order to
make a word into something completely different it is not enough to move the
syllables around. The syllables themselves should be destroyed.

Take, for instance, the word biscuit. If we naively move a few syllables around,
you can still kind of make it: cuitbis. No letter is in the same position as it
was before, yet, anyone can easily put together the original word. Let's collect
the digrams for that word then:

    bi, sc, cu, it

Out of all anagrams we can make out from biscuit, the ones which have those
digrams are probably easier to figure out than those which don't. Well, except
when you consider the following:

    tiucsib

Any sort of mirror will reveal the secret right off. No good! Also, bsiucti
doesn't seem that hard, even though there was some serious swapping around. So,
let's expand our digrams a little. Let's also add the reverse. Thus, our digrams
are:

    bi, ib, sc, cs, cu, uc, it, ti

Now we can say that

    bciisut

is a great deal apart from biscuit. However, starting and finishing with the
same letters doesn't seem perfect, we can do better! Let's also consider the
start and end boundaries:

    ^b, bi, ib, sc, cs, cu, uc, it, ti, t$

Now, if we go through all the anagrams and find the ones in which those digrams
show up the least we should have a very well scrambled word. This one of the
farthest away anagrams considering our metric:

    iicbstu

The problem is: how to do that efficiently?

Qualitative analysis
--------------------

Here are a few examples. The first level represents the original word.

| level | anagrams |
|-------|----------|
|     0 | rocks |
|     2 | skcor |
|     3 | corks, rskco, orcks, rocsk, kcors, roskc |
|     4 | cksor, skroc, ocksr, cksro, rcoks, rkcos, srock, kscor, ksroc, skcro, corsk, orskc, rokcs |
|     5 | rsock, rskoc, orkcs, ocrks, krocs, rckso, rksoc, roksc, rksco, kcros, rcosk, ckros, ckors, croks, ockrs, rosck |
|     6 | skorc, sockr, sckor, kcosr, srkco, sorkc, skrco, oskcr, orcsk, ocrsk, rckos, crosk, sorck, ocskr, kcsro, ksocr, cskro, coskr, ksrco, coksr, skocr, rkocs, ksorc, kscro, kcsor, sckro, scork, orksc, cskor, srokc, orsck |
|     7 | korcs, kocrs, rsokc, cokrs, krcos, rscok, rcsko, rkcso, rscko, okcrs |
|     8 | srkoc, srcko, cosrk, scokr, okcsr, okscr, socrk, srcok, krsco, kocsr, oksrc, osckr, csrok, crsko, crkso, korsc, ckrso, csork, ckosr, sokcr, scrok, oskrc, ocsrk, krsoc, krosc, osrck, osrkc, kcrso |
|     9 | crkos, rkosc, rcsok, okrcs |
|     10| krcso, oscrk, scrko, okrsc, csokr, koscr, csrko, kosrc, crsok, sokrc |

| level | anagrams |
|-------|----------|
|     0 | fame |
|     2 | emaf |
|     3 | mafe, faem, fema, afme |
|     4 | afem, emfa, meaf, fmae, mefa, efam, amef |
|     5 | mfae, amfe, fmea, feam |
|     6 | efma, eamf, eafm, maef, aemf |
|     8 | mfea, aefm |


| level  | anagrams |
|--------|----------|
|     0  | banana |
|     2  | ananab |
|     3  | baanan, anabna, anbana, ananba, banaan, nanaba, nabana, abnana |
|     4  | abanan, bnanaa, bnaana, anaban, bannaa, baanna, naanab, nanaab |
|     5  | abanna, annaba, naabna, nanbaa, nbanaa, nabnaa, nbaana, naanba |
|     6  | naaban, aananb, anbaan, anaabn, aanban, aanabn, annaab, aannab, aabnan, anaanb, abnaan, nabaan |
|     7  | aabnna, aannba, anbnaa, nnabaa, nnaaba, baaann, aanbna, abnnaa, annbaa, bnaaan |
|     8  | aabann, naaabn, nnaaab, bnnaaa, abaann, nbaaan, naaanb |
|     9  | nbnaaa, nnbaaa |
|     10 | aaabnn, aaannb, aaanbn |
