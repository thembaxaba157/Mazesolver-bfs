import world.text.world as rob_world
import unittest


class WorldTestCase(unittest.TestCase):
    def test_generate_obstacles(self):

        rob_world.generate_world_obstacle([(4,0),(9,2),(80,50)])
        self.assertEqual(rob_world.obs.rob_obstacles,[(4,0),(9,2),(80,50)])

    def test_forward_with_obstacle_message(self):
        rob_world.obs.rob_obstacles = [(0,10)]
        result = rob_world.do_forward('HAL',10)
        self.assertEqual((True, ' > HAL Sorry, there is an obstacle in the way.'),result)

    def test_back_with_obstacle_message(self):
        rob_world.obs.rob_obstacles = [(0,-10)]
        result = rob_world.do_back('HAL',10)
        self.assertEqual((True, ' > HAL Sorry, there is an obstacle in the way.'),result)

    def test_forward_with_obstacle_message2(self):
        rob_world.obs.rob_obstacles = [(0,10)]
        result = rob_world.do_forward('HAL',50)
        self.assertEqual((True, ' > HAL Sorry, there is an obstacle in the way.'),result)
    
    def test_forward_with_obstacle_message3(self):
        rob_world.obs.rob_obstacles = [(0,10)]
        result = rob_world.do_forward('HAL',9)
        self.assertEqual((True, ' > HAL moved forward by 9 steps.'),result)
    
        

if __name__ == '__main__':
    unittest.main()
