# https://github.com/MrJoethBobeth/lab10-LM-NL
# Partner 1: Luis Malave Matias
# Partner 2: Nathan Lohnes

import unittest
import calculator
import math

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-5, -5), -10)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)
        self.assertEqual(calculator.subtract(-1, 1), -2)
        self.assertEqual(calculator.subtract(5, 10), -5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 10)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithim(10, 100), 2)
        self.assertAlmostEqual(calculator.logarithim(2, 8), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithim(1, 100)
        with self.assertRaises(ValueError):
            calculator.logarithim(0, 100)
        with self.assertRaises(ValueError):
            calculator.logarithim(-2, 100)
        with self.assertRaises(ValueError):
            calculator.logarithim(10, 0)
        with self.assertRaises(ValueError):
            calculator.logarithim(10, -10)

    def test_square_root(self):
        self.assertAlmostEqual(calculator.square_root(9), 3)
        self.assertAlmostEqual(calculator.square_root(144), 12)
        self.assertAlmostEqual(calculator.square_root(0), 0)

    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            calculator.square_root(-1)
        with self.assertRaises(ValueError):
            calculator.square_root(-100)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13)

if __name__ == '__main__':
    unittest.main()
