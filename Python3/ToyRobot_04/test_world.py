import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
from world.text import world
import robot

class TestWorld(unittest.TestCase):
    def test_do_back(self):
        output = world.do_back('al',5)
        correct = (True, ' > al moved back by 5 steps.')
        self.assertEqual(output,correct)

    def test_do_forward(self):
        output = world.do_forward('al', 5)
        correct = (True, ' > al moved forward by 5 steps.')
        self.assertEqual(output,correct)

    def test_left_turn(self):
        output = world.do_left_turn('al')
        correct = (True, ' > al turned left.')
        self.assertEqual(output,correct)

    def test_right_turn(self):
        output = world.do_right_turn('al')
        correct = (True, ' > al turned right.')
        self.assertEqual(output,correct)

    def test_is_position_allowed(self):
        output = world.is_position_allowed(0,0)
        correct = True
        self.assertEqual(output,correct)

    def test_left_turn(self):
        output = world.show_position('al')
        print(output)
        correct = (None)
        self.assertEqual(output,correct)
