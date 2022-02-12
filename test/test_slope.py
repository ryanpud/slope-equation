import unittest
from src import slope

class TestSlope(unittest.TestCase):
    def test_oper1(self):
        result5 = slope.oper1(6,3)
        self.assertEqual(result5, 2)
    def test_oper2(self):
        result6 = slope.oper2(6,3)
        self.assertEqual(result6, 2)