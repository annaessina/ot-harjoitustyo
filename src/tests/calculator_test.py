import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        calc1 = Calculator()


    def test_add_number_oikein(self):
        self.calc1.kaynnista()

        self.assertEqual(self.calc1, number1+number2)