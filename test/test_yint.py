import unittest
import yint


class TestSlope(unittest.TestCase):

    def test_yinttest1(self):
        result = input.yint_multiply(5, 3)
        self.assertEqual(result, 15)
    
    def test_yinttest2(self):
        result2 = input.yint_final(5, 3)
        self.assertEqual(result2, 2)
