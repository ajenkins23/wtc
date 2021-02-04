import random
import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import robot


class TestRobot(unittest.TestCase):
    def test_Replay(self):
        with captured_io(StringIO('al\nforward 10\nforward 5\nreplay\noff')) as (out,err):
            robot.robot_start()
        
        output = out.getvalue()
        replay = '''What do you want to name your robot? al: Hello kiddo!
al: What must I do next?  > al moved forward by 10 steps.
 > al now at position (0,10).
al: What must I do next?  > al moved forward by 5 steps.
 > al now at position (0,15).
al: What must I do next?  > al moved forward by 10 steps.
 > al now at position (0,25).
 > al moved forward by 5 steps.
 > al now at position (0,30).
 > al replayed 2 commands.
 > al now at position (0,30).
al: What must I do next? al: Shutting down..
'''
        self.assertEqual(output, replay)

    def test_ReplaySilent(self):
        with captured_io(StringIO('al\nforward 10\nforward 5\nreplay silent\noff')) as (out,err):
            robot.robot_start()
        
        output = out.getvalue()
        replay = '''What do you want to name your robot? al: Hello kiddo!
al: What must I do next?  > al moved forward by 10 steps.
 > al now at position (0,10).
al: What must I do next?  > al moved forward by 5 steps.
 > al now at position (0,15).
al: What must I do next?  > al replayed 2 commands silently.
 > al now at position (0,30).
al: What must I do next? al: Shutting down..
'''
        self.assertEqual(output, replay)

    def test_ReplayReverse(self):
        with captured_io(StringIO('al\nforward 10\nforward 5\nreplay reversed\noff')) as (out,err):
            robot.robot_start()
        
        output = out.getvalue()
        replay = '''What do you want to name your robot? al: Hello kiddo!
al: What must I do next?  > al moved forward by 10 steps.
 > al now at position (0,10).
al: What must I do next?  > al moved forward by 5 steps.
 > al now at position (0,15).
al: What must I do next?  > al moved forward by 5 steps.
 > al now at position (0,20).
 > al moved forward by 10 steps.
 > al now at position (0,30).
 > al replayed 2 commands in reverse.
 > al now at position (0,30).
al: What must I do next? al: Shutting down..
'''
        self.assertEqual(output, replay)

    def test_ReplayReverseSilent(self):
        with captured_io(StringIO('al\nforward 10\nforward 5\nreplay reversed\noff')) as (out,err):
            robot.robot_start()
        
        output = out.getvalue()
        replay = '''What do you want to name your robot? al: Hello kiddo!
al: What must I do next?  > al moved forward by 10 steps.
 > al now at position (0,10).
al: What must I do next?  > al moved forward by 5 steps.
 > al now at position (0,15).
al: What must I do next?  > al moved forward by 5 steps.
 > al now at position (0,20).
 > al moved forward by 10 steps.
 > al now at position (0,30).
 > al replayed 2 commands in reverse.
 > al now at position (0,30).
al: What must I do next? al: Shutting down..
'''
        self.assertEqual(output, replay)