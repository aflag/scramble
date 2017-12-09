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
show up the least we should have a very well scrambled word. The problem is: how
to do that efficiently?
