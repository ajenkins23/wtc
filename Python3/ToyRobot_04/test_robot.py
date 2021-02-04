import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import world.obstacles as obstacles
import robot

class TestRobot(unittest.TestCase):

    def test_off(self):
        obstacles.random.randint = lambda a,b:0
        with captured_io(StringIO('al\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? al: Hello kiddo!
al: What must I do next? al: Shutting down..""", output)

    def test_fwd_100_off(self):
        obstacles.random.randint = lambda a,b:0
        with captured_io(StringIO('al\nforward 100\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? al: Hello kiddo!
al: What must I do next?  > al moved forward by 100 steps.
 > al now at position (0,100).
al: What must I do next? al: Shutting down..""", output)

    def test_fwd_201_off(self):
        obstacles.random.randint = lambda a,b:0
        with captured_io(StringIO('al\nforward 201\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? al: Hello kiddo!
al: What must I do next? al: Sorry, I cannot go outside my safe zone.
 > al now at position (0,0).
al: What must I do next? al: Shutting down..""", output)

    def test_help_off(self):
        obstacles.random.randint = lambda a,b:0
        with captured_io(StringIO('al\nhelp\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? al: Hello kiddo!
al: What must I do next? I can understand these commands:
OFF  - Shut down robot
HELP - provavaidiblen right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]

 > al now at position (0,0).
al: What must I do next? al: Shutting down..""", output)

    def test_right_left_off(self):
        obstacles.random.randint = lambda a,b:0
        with captured_io(StringIO('al\nright\nleft\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? al: Hello kiddo!
al: What must I do next?  > al turned right.
 > al now at position (0,0).
al: What must I do next?  > al turned left.
 > al now at position (0,0).
al: What must I do next? al: Shutting down..""", output)

    def test_camel_commands(self):
        obstacles.random.randint = lambda a,b:0
        with captured_io(StringIO('al\nHelp\nForWaRd 10\nBaCk 10\nRiGhT\nLeFt\noff')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? al: Hello kiddo!
al: What must I do next? I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]

 > al now at position (0,0).
al: What must I do next?  > al moved forward by 10 steps.
 > al now at position (0,10).
al: What must I do next?  > al moved back by 10 steps.
 > al now at position (0,0).
al: What must I do next?  > al turned right.
 > al now at position (0,0).
al: What must I do next?  > al turned left.
 > al now at position (0,0).
al: What must I do next? al: Shutting down..""", output)

    def test_fwd_10_back_10_replay(self):
        obstacles.random.randint = lambda a,b:0
        with captured_io(StringIO('al\nforward 10\nback 10\nreplay\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? al: Hello kiddo!
al: What must I do next?  > al moved forward by 10 steps.
 > al now at position (0,10).
al: What must I do next?  > al moved back by 10 steps.
 > al now at position (0,0).
al: What must I do next?  > al moved forward by 10 steps.
 > al now at position (0,10).
 > al moved back by 10 steps.
 > al now at position (0,0).
 > al replayed 2 commands.
 > al now at position (0,0).
al: What must I do next? al: Shutting down..""", output)

    def test_wrong_commands(self):
        obstacles.random.randint = lambda a,b:0
        with captured_io(StringIO('al\nHel\nForWaR 10\nBaC 10\nRiGh\nLeF\nof\noff\n')) as (out, err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? al: Hello kiddo!
al: What must I do next? al: Sorry, I did not understand 'Hel'.
al: What must I do next? al: Sorry, I did not understand 'ForWaR 10'.
al: What must I do next? al: Sorry, I did not understand 'BaC 10'.
al: What must I do next? al: Sorry, I did not understand 'RiGh'.
al: What must I do next? al: Sorry, I did not understand 'LeF'.
al: What must I do next? al: Sorry, I did not understand 'of'.
al: What must I do next? al: Shutting down..""", output)