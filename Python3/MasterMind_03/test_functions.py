import unittest
from io import StringIO
import sys
from test_base import captured_io
from test_base import run_unittests
import mastermind as ms
import subprocess

class TestCases(unittest.TestCase):
    def test_Within_Range(self):
        within_range = True
        for x in range(100):
            code = ms.create_code()
            if 9 in code or 0 in code:
                within_range = False
        self.assertEqual(1, within_range)

    def test_Update_Correctness(self):
        with captured_io(''):
            self.assertEqual(ms.check_correctness(1,4,0), True)
            self.assertEqual(ms.check_correctness(1,3,0), False)

    def test_User_Input(self):
        with captured_io(StringIO('123\n1234\n123')):
            self.assertEqual(len(ms.getUserInput()), 4)

    def test_Take_Turns(self):
        code = [1,2,3,4]
        with captured_io(StringIO('1234\n2341\n1243\n1278\n2178')):
            correct_digit = ms.take_turn(code)
            self.assertEqual((correct_digit[0], correct_digit[1]),(4, 0))
            correct_digit = ms.take_turn(code)
            self.assertEqual((correct_digit[0], correct_digit[1]),(0, 4))
            correct_digit = ms.take_turn(code)
            self.assertEqual((correct_digit[0], correct_digit[1]),(2, 2))
            correct_digit = ms.take_turn(code)
            self.assertEqual((correct_digit[0], correct_digit[1]),(2, 0))
            correct_digit = ms.take_turn(code)
            self.assertEqual((correct_digit[0], correct_digit[1]),(0, 2))