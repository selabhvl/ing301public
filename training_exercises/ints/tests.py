import sys
from pathlib import Path
import unittest

thisfile = Path(__file__)
sys.path.append(str(thisfile.parent))


from exercises import *


class IntTests(unittest.TestCase):

    def test_square_basic(self):
        self.assertEqual(0, square(0))
        self.assertEqual(1, square(1))
        self.assertEqual(4, square(2))
        self.assertEqual(25, square(5))
        self.assertEqual(9, square(-3))

    def test_max2(self):
        self.assertEqual(5, max2(5, 3))
        self.assertEqual(0, max2(0, -2))

    def test_max3(self):
        self.assertEqual(7, max3(7, 3, 4))
        self.assertEqual(-1, max3(-5, -1, -3))

    def test_average(self):
        self.assertAlmostEqual(2.5, average(2, 3))
        self.assertAlmostEqual(-1.5, average(-2, -1))

    def test_average3(self):
        self.assertAlmostEqual(2.0, average3(1, 2, 3))
        self.assertAlmostEqual(0.0, average3(-1, 0, 1))

    def test_factorial(self):
        self.assertEqual(1, factorial(0))
        self.assertEqual(120, factorial(5))
        self.assertEqual(3628800, factorial(10))

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_product(self):
        self.assertEqual(24, product(1, 4))
        self.assertEqual(3, product(3, 3))

    def test_sum(self):
        self.assertEqual(10, sum(1, 4))
        self.assertEqual(0, sum(-1, 1))

    def test_fib(self):
        self.assertEqual(1, fib(0))
        self.assertEqual(1, fib(1))
        self.assertEqual(8, fib(5))

    def test_fib_negative(self):
        with self.assertRaises(ValueError):
            fib(-5)

    def test_is_prime(self):
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(18))

    def test_reverse(self):
        self.assertEqual(4321, reverse(1234))
        self.assertEqual(21, reverse(1200))

if __name__ == "__main__":
    unittest.main()

