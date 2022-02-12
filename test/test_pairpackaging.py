import unittest
from src import pairpackaging

class TestPairPackaging(unittest.TestCase):
        def test_pair1(self):
            result = pairpackaging.pair1(5,3)
            self.assertEqual(result, '(5,3)')
    
        def test_pair2(self):
            result = pairpackaging.pair2(5,3)
            self.assertEqual(result, '(5,3)')
        