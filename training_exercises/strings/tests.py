import sys
from pathlib import Path
import unittest

thisfile = Path(__file__)
sys.path.append(str(thisfile.parent))


from exercises import *


class StringTests(unittest.TestCase):

    def test_length(self):
        self.assertEqual(0, length(""))
        self.assertEqual(1, length('H'))
        self.assertEqual(5, length("hallo"))

    def test_reverse(self):
        self.assertEqual("", reverse(""))
        self.assertEqual("olleh", reverse("hello"))
        self.assertEqual("madam", reverse("madam"))

    def test_starts_with(self):
        self.assertTrue(starts_with("hello", "hel"))
        self.assertFalse(starts_with("hello", "lo"))
        self.assertFalse(starts_with("", "a"))

    def test_ends_with(self):
        self.assertTrue(ends_with("testing", "ing"))
        self.assertFalse(ends_with("testing", "test"))
        self.assertTrue(ends_with("", ""))

    def test_contains(self):
        self.assertTrue(contains("pineapple", "apple"))
        self.assertFalse(contains("pineapple", "banana"))
        self.assertTrue(contains("pineapple", ""))

    def test_contains_how_often(self):
        self.assertEqual(0, contains_how_often("", ""))
        self.assertEqual(3, contains_how_often("aaaa", "aa"))
        self.assertEqual(1, contains_how_often("hello", "ll"))

    def test_first_index_of(self):
        self.assertEqual(2, first_index_of("banana", "n"))
        self.assertEqual(-1, first_index_of("banana", "z"))
        self.assertEqual(0, first_index_of("abc", "a"))

    def test_last_index_of(self):
        self.assertEqual(4, last_index_of("mississippi", "issi"))
        self.assertEqual(-1, last_index_of("mississippi", "xyz"))
        self.assertEqual(0, last_index_of("a", "a"))

    def test_index_of_after(self):
        self.assertEqual(3, index_of_after("ababa", "ba", 1))
        self.assertEqual(-1, index_of_after("ababa", "ba", 3))
        self.assertEqual(1, index_of_after("ababa", "ba", 0))

    def test_sub_string(self):
        self.assertEqual("ban", sub_string("banana", 1, 4))
        self.assertEqual("", sub_string("banana", 2, 2))
        self.assertEqual("banana", sub_string("banana", 0, 6))

    def test_remove_first(self):
        self.assertEqual("baba", remove_first("ababa", "a"))
        self.assertEqual("hello", remove_first("hello", "z"))
        self.assertEqual("", remove_first("aa", "aa"))

    def test_remove_all(self):
        self.assertEqual("", remove_all("aaa", "a"))
        self.assertEqual("ba", remove_all("banana", "nan"))
        self.assertEqual("hello", remove_all("hello", "z"))

    def test_less(self):
        self.assertTrue(less("abc", "b"))
        self.assertFalse(less("b", "abc"))
        self.assertFalse(less("abc", "abc"))

    def test_to_roman(self):
        self.assertEqual("I", to_roman(1))
        self.assertEqual("IV", to_roman(4))
        self.assertEqual("MMXXIV", to_roman(2024))
        self.assertEqual("MCMXCIV", to_roman(1994))

    def test_replace_first(self):
        self.assertEqual("hello world", replace_first("hello hello", "hello", "*"))
        self.assertEqual("hello world", replace_first("hello world", "x", "y"))
        self.assertEqual("xy", replace_first("xx", "x", "xy"))

    def test_replace_all(self):
        self.assertEqual("xyxy", replace_all("abab", "a", "xy"))
        self.assertEqual("hello", replace_all("hello", "z", "x"))
        self.assertEqual("", replace_all("aaa", "a", ""))


if __name__ == "__main__":
    unittest.main()
