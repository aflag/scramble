"""
This module defines a distance between two anagrams and two methods that can be
used to find the most different anagram for a given string.
"""
from functools import partial
from itertools import permutations


def get_anagram_distance(s1, s2):
    """
    Returns the anagram distance between two anagrams. The two strings must
    have the same size and be anagrams (the latter is not checked).

    The anagram distance is directly proportional to the number of digrams the
    two strings have in common. However, for this algorithm, the digram meaning
    was extrapolated to ignore the order of the characters and to consider the
    end and beginning of the string as part of a digram.

    Take the two strings hey and yeh:
    
        - hey has the following digrams:
            ('h', 'e'), ('e', 'h'), ('e', 'y'), ('y', 'e'), ('', 'h'), ('y', '')
        - eyh has the following digrams:
            ('e', 'y'), ('y', 'e'), ('y', 'h'), ('h', 'y'), ('', 'e'), ('h', '')

    They both have the same number of digrams, 6 (that's the maximum distance).
    However, they share 2 digrams. Therefore the distance between them is 4.
    """
    assert len(s1) == len(s2)
    s1_digrams = _digrams(s1)
    s2_digrams = _digrams(s2)
    for e in s2_digrams:
        try:
            s1_digrams.remove(e)
        except ValueError:
            pass
    return len(s1_digrams)


def get_all_distances(s):
    """This method tries all permutations of s and calculate their distance
    based on get_anagram_distance"""
    distances = {}
    for s2 in permutations(s):
        s2 = ''.join(s2)
        distance = get_anagram_distance(s, s2)
        distances.setdefault(distance, set()).add(s2)
    return distances


def scramble(s):
    """This is a greedy algorithm which attempts to compute the most distant
    string from s, as measured with get_anagram_distance. It may result in
    suboptimal results. The run time is O(n^2)"""
    digrams = set(_digrams(s))
    scrambled = list(s)
    for i in range(len(scrambled)):
        for j in range(i, len(scrambled)):
            if (_prev(scrambled, i), scrambled[j]) not in digrams:
                scrambled[i], scrambled[j] = scrambled[j], scrambled[i]
                break
    return ''.join(scrambled)


def _prev(scrambled, i):
    if i - 1 < 0:
        return ""
    else:
        return scrambled[i - 1]


def _digrams(s):
    if not s:
        return []
    reverse = s[::-1]
    d_normal = list(zip(s, s[1:]))
    d_reverse = list(zip(reverse, reverse[1:]))
    d_border = [("", s[0]), (s[-1], "")]
    return d_normal + d_reverse + d_border


def _swaps(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            yield i, j


def _swap(s, i, j):
    s2 = list(s)
    s2[i], s2[j] = s2[j], s2[i]
    return "".join(s2)
