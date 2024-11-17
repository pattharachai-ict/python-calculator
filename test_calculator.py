import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()  # Initialize the Calculator object

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)  # Test addition with positive numbers
        self.assertEqual(self.calc.add(0, 5), 5)  # Test addition with zero

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)  # Test subtraction with positive result
        self.assertEqual(self.calc.subtract(3, 5), -2)  # Test subtraction with negative result

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)  # Test multiplication with positive numbers
        self.assertEqual(self.calc.multiply(0, 5), 0)  # Test multiplication with zero

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3)  # Test division with positive numbers
        with self.assertRaises(ValueError):  # Test division by zero
            self.calc.divide(5, 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)  # Test modulo operation
        with self.assertRaises(ValueError):  # Test modulo by zero
            self.calc.modulo(5, 0)

if __name__ == "__main__":
    unittest.main()
