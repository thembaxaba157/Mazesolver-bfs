import unittest
import robot
from unittest.mock import patch
from io import StringIO
import sys
import maze.obstacles as obstacles

obstacles.random.randint = lambda a,b: 0

class BasicCommandsTestCase(unittest.TestCase):
    @patch("sys.stdin", StringIO("HAL\nHelp\noff"))
    def test_full_help_off(self):
        self.maxDiff = None
        sys.stdout = StringIO()
        robot.robot_start()
        output = sys.stdout.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: Loaded obstacles.
HAL: What must I do next? I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]""", output[:538])


    @patch("sys.stdin", StringIO("HAL\nsprint 30\noff"))
    def test_sprint_30(self):
       
        sys.stdout = StringIO()
        robot.robot_start()

        output = sys.stdout.getvalue().strip()

        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: Loaded obstacles.
HAL: What must I do next?  > HAL moved forward by 30 steps.
 > HAL moved forward by 29 steps.
 > HAL moved forward by 28 steps.
 > HAL moved forward by 27 steps.
 > HAL moved forward by 26 steps.
 > HAL moved forward by 25 steps.
 > HAL moved forward by 24 steps.
HAL: Sorry, I cannot go outside my safe zone.
HAL: Sorry, I cannot go outside my safe zone.
HAL: Sorry, I cannot go outside my safe zone.
HAL: Sorry, I cannot go outside my safe zone.
HAL: Sorry, I cannot go outside my safe zone.
HAL: Sorry, I cannot go outside my safe zone.
HAL: Sorry, I cannot go outside my safe zone.
HAL: Sorry, I cannot go outside my safe zone.
HAL: Sorry, I cannot go outside my safe zone.
HAL: Sorry, I cannot go outside my safe zone.
HAL: Sorry, I cannot go outside my safe zone.
HAL: Sorry, I cannot go outside my safe zone.
 > HAL moved forward by 11 steps.
HAL: Sorry, I cannot go outside my safe zone.
HAL: Sorry, I cannot go outside my safe zone.
HAL: Sorry, I cannot go outside my safe zone.
HAL: Sorry, I cannot go outside my safe zone.
HAL: Sorry, I cannot go outside my safe zone.
HAL: Sorry, I cannot go outside my safe zone.
HAL: Sorry, I cannot go outside my safe zone.
HAL: Sorry, I cannot go outside my safe zone.
HAL: Sorry, I cannot go outside my safe zone.
HAL: Sorry, I cannot go outside my safe zone.
 > HAL now at position (0,200).
HAL: What must I do next? HAL: Shutting down..""",output)

class TestReplay(unittest.TestCase):
    @patch("sys.stdin", StringIO('HAL\nreplay\noff\n'))
    def test_replay_without_previous_commands(self):
        sys.stdout = StringIO()
        robot.robot_start()

        output = sys.stdout.getvalue().strip()
        self.assertEqual(output,f'''What do you want to name your robot? HAL: Hello kiddo!
HAL: Loaded obstacles.
HAL: What must I do next?  > HAL replayed 0 commands.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down..''')

    @patch("sys.stdin", StringIO('HAL\nforward 3\nforward 2\nforward 1\nreplay 3 reversed silent\noff\n'))
    def test_replay_range_basic_silent_reversed(self):
        sys.stdout = StringIO()
        robot.robot_start()
        self.maxDiff = None
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output,'''What do you want to name your robot? HAL: Hello kiddo!
HAL: Loaded obstacles.
HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,3).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL moved forward by 1 steps.
 > HAL now at position (0,6).
HAL: What must I do next?  > HAL replayed 3 commands in reverse silently.
 > HAL now at position (0,12).
HAL: What must I do next? HAL: Shutting down..''')

    
    @patch("sys.stdin", StringIO('HAL\nforward 3\nforward 2\nforward 1\nreplay 3-1 silent\noff\n'))
    def test_replay_range_full_silent(self):
        sys.stdout = StringIO()
        robot.robot_start()

        output = sys.stdout.getvalue().strip()
        self.assertEqual(output,'''What do you want to name your robot? HAL: Hello kiddo!
HAL: Loaded obstacles.
HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,3).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL moved forward by 1 steps.
 > HAL now at position (0,6).
HAL: What must I do next?  > HAL replayed 2 commands silently.
 > HAL now at position (0,11).
HAL: What must I do next? HAL: Shutting down..''')

    @patch("sys.stdin", StringIO('HAL\nforward 3\nforward 2\nforward 1\nreplay 3-1 reversed silent\noff\n'))
    def test_replay_range_full_silent_reversed(self):
        sys.stdout = StringIO()
        robot.robot_start()

        output = sys.stdout.getvalue().strip()
        self.assertEqual(output,'''What do you want to name your robot? HAL: Hello kiddo!
HAL: Loaded obstacles.
HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,3).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL moved forward by 1 steps.
 > HAL now at position (0,6).
HAL: What must I do next?  > HAL replayed 2 commands in reverse silently.
 > HAL now at position (0,9).
HAL: What must I do next? HAL: Shutting down..''')

if __name__=='__main__':
    unittest.main()
