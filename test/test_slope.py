import unittest
from src import slope

class TestSlope(unittest.TestCase):
    def test_oper1(self):
        result = slope.oper1(6,3)
        self.assertEqual(result, 3)
    def test_slope_final(self):
         result = slope.slope_final(6,3)
         self.assertEqual(result, 2)  