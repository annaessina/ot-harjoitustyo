import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.Calculator = Calculator()
        self.Calculator.number1 = 8
        self.Calculator.number2 = 3

    def test_add_oikein(self):

        self.assertEqual(self.Calculator.add(), 11)

    def test_dist_oikein(self):
        self.assertEqual(self.Calculator.dist(), 5)