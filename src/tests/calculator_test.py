import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.Calculator = Calculator()
        self.Calculator.number1 = 9
        self.Calculator.number2 = 3

    def test_add_oikein(self):
        self.assertEqual(self.Calculator.add(), 12)

    def test_dist_oikein(self):
        self.assertEqual(self.Calculator.dist(), 6)

    def test_mult_oikein(self):
        self.assertEqual(self.Calculator.mult(), 27)

    def test_div_oikein(self):
        self.assertEqual(self.Calculator.div(), 3)
