import unittest
from src import yint

class TestYint(unittest.TestCase):
    def test_yinttest1(self):
        result = yint.yint_multiply(5, 3)
        self.assertEqual(result, 15)
    
    def test_yinttest2(self):
        result = yint.yint_final(5, 3)
        self.assertEqual(result, 2)
