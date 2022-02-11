import unittest

class slopetest(unittest.TestCase):
    def yinttest1(self):
        result = input.yint_multiply(5, 3)
        self.assertEqual(result, 15)
    
    def yinttest2(self):
        result2 = input.yint_final(5, 3)
        self.assertEqual(result2, 2)
        
