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


class GetAllDistancesTestCase(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(scramble.get_all_distances(""), {0: {""}})

    def test_two_chars(self):
        expected = {
            0: {"ab"},
            2: {"ba"},
        }
        self.assertEqual(scramble.get_all_distances("ab"), expected)

    def test_repeated(self):
        expected = {
            0: {"aa"},
        }
        self.assertEqual(scramble.get_all_distances("aa"), expected)

    def test_abc(self):
        expected = {
            0: {"abc"},
            2: {"cba"},
            3: {"acb", "bac"},
            4: {"cab", "bca"},
        }
        self.assertEqual(scramble.get_all_distances("abc"), expected)


class ScrambleTestCase(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(scramble.scramble(""), "")

    def test_one_letter(self):
        self.assertEqual(scramble.scramble("a"), "a")

    def test_two_letters(self):
        self.assertEqual(scramble.scramble("ab"), "ba")

    def test_same_letters(self):
        self.assertEqual(scramble.scramble("aa"), "aa")

    def test_small_word(self):
        scrambled = scramble.scramble("fact")
        self.assertEqual(set(scrambled), set("fact"))
        self.assertEqual(len(scrambled), len("fact"))
        self.assertNotEqual(scrambled, "fact")
