import unittest
import sys
from test_base import run_unittests, StringIO, captured_io
import super_algos as SA

class test_algos(unittest.TestCase):
    def testFindMinNormal(self): 
        with captured_io(''):
            res = [1,2,3,4]
            self.assertEqual(SA.find_min(res), 1)

    def testFindMinEmpty(self):
        with captured_io(''):
            res = []
            self.assertEqual(SA.find_min(res), -1)

    def testFindMinTuple(self):
        with captured_io(''):
            res = (1,2,3)
            self.assertEqual(SA.find_min(res), 1)
    
    def testFindMinString(self):
        with captured_io(''):
            res = ['1', '2', '3']
            self.assertEqual(SA.find_min(res), -1)

    def testSumNormal(self):
        res = [1,2,3,4]
        with captured_io(''):
            self.assertEqual(SA.sum_all(res), 10)
        
    def testSumEmpty(self):
        with captured_io(''):
            res = []
            self.assertEqual(SA.sum_all(res), -1)

    def testSumTuple(self):
        with captured_io(''):
            res = (1,2,3,4)
            self.assertEqual(SA.sum_all(res), 10)
    
    def testSumString(self):
        with captured_io(''):
            res = ['1', '2', '3']
            self.assertEqual(SA.sum_all(res), -1)
    
    def testPermutationNormal(self):
        with captured_io(''):
            res = ['a', 'b']
            self.assertEqual(len(SA.find_possible_strings(res, len(res))), 4)
            self.assertEqual(SA.find_possible_strings(res, len(res)), ['aa', 'ab', 'ba', 'bb'])
    
    def testPermutationInt(self):
        with captured_io(''):
            res = [1, 2, 3, 4]
            self.assertEqual(SA.find_possible_strings(res, len(res)), [])