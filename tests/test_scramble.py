import unittest

import scramble


class GetDistanceTestCase(unittest.TestCase):

    def test_different_sizes(self):
        self.assertRaises(AssertionError, scramble.get_anagram_distance, "asd", "asdf")

    def test_empty_string(self):
        self.assertEqual(scramble.get_anagram_distance("", ""), 0)

    def test_equal_strings(self):
        self.assertEqual(scramble.get_anagram_distance("abcd", "abcd"), 0)

    def test_very_different(self):
        self.assertEqual(scramble.get_anagram_distance("fact", "atfc"), 8)


class BestScrambleTestCase(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(scramble.best_scramble(""), "")

    def test_fact(self):
        self.assertEqual(scramble.best_scramble("fact"), "atfc")


class ScrambleTestCase(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(scramble.scramble(""), "")

    def test_small_word(self):
        self.assertEqual(scramble.scramble("fact"), "cfta")

    def test_big_sentence(self):
        self.assertEqual(scramble.scramble("I am writing a big sentence here."), "eeegeew.tr   ii iabsn nmgct nIrha")