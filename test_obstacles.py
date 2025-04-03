import maze.obstacles as obs 
import unittest
from unittest.mock import patch
from io import StringIO
import sys





class TestObstaclesFile(unittest.TestCase):
    obs.rob_obstacles = [(4,4)]
    
    def test_is_path_blocked_true(self):
        obs.rob_obstacles = [(4,4)]
        self.assertTrue(obs.is_path_blocked(4,2,4,10))

    def test_is_path_blocked_true_inbetween(self):
        obs.rob_obstacles = [(4,4)]
        self.assertTrue(obs.is_path_blocked(5,2,5,10))
    
    def test_is_path_blocked_False(self):
        obs.rob_obstacles = [(4,4)]
        self.assertFalse(obs.is_path_blocked(9,2,9,10))

    def test_is_position_blocked_true(self):
        obs.rob_obstacles = [(4,4)]
        self.assertTrue(obs.is_position_blocked(5,5))

    def test_is_position_blocked_false(self):
        obs.rob_obstacles = [(4,4)]
        self.assertFalse(obs.is_position_blocked(9,9))

if __name__=='__main__':
    unittest.main()