import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        calc1 = Calculator(5,3)


    def test_add_number_oikein(self):
        self.calc1.kaynnista()

        self.assertEqual(self.calc1, 8)

