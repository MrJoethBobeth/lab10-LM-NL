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
        self.assertAlmostEqual(calculator.logarithm(10, 100), 2)
        self.assertAlmostEqual(calculator.logarithm(2, 8), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 100)
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 100)
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 100)
        with self.assertRaises(ValueError):
            calculator.logarithm(10, 0)
        with self.assertRaises(ValueError):
            calculator.logarithm(10, -10)

    def test_sqrt(self):
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

    def test_multiply(self):
        self.assertAlmostEqual(calculator.mul(3, 3), 9)
        self.assertAlmostEqual(calculator.mul(-2, 2), -4)
        self.assertAlmostEqual(calculator.mul(-1, -20), 20)

    def test_divide(self):
        self.assertAlmostEqual(calculator.div(5, 1), 5)
        self.assertAlmostEqual(calculator.div(-4, 2), -2)
        self.assertAlmostEqual(calculator.div(-9, -3), 3)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(-1, 3)
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 3)
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 3)
        with self.assertRaises(ValueError):
            calculator.logarithm(10, 0)
        with self.assertRaises(ValueError):
            calculator.logarithm(10, -2)


        
if __name__ == '__main__':
    unittest.main()
