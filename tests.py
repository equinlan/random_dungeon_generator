import dungeon_generator as dungen
import unittest

class TestGameMapInit(unittest.TestCase):
    def test_width(self):
        width = 10
        map = dungen.GameMap(width, 20)
        self.assertEqual(map.width, width, 'The map did not correctly set its width.')
    
    def test_height(self):
        height = 20
        map = dungen.GameMap(10, height)
        self.assertEqual(map.height, height, 'The map did not correctly set its height.')
    
    def test_zeros(self):
        # Should set map size to minimum of 1
        map = dungen.GameMap(0, 0)
        self.assertEqual((map.width, map.height), (1, 1), 'The map allowed itself to be set to 0 width or height.')

class TestGetNeighbors(unittest.TestCase):
    def setUp(self):
        try:
            self.map = dungen.GameMap(10, 20)
        except:
            self.fail('Could not construct dungeon.')

    def test_get_at_corner(self):
        x, y = 0, 0
        neighbors = self.map.get_neighbors(x, y)
        self.assertEqual(len(neighbors), 2, 'Incorrect neighbor count returned for corner.')
    
    def test_get_at_center(self):
        x, y = 5, 10
        neighbors = self.map.get_neighbors(x, y)
        self.assertEqual(len(neighbors), 4, 'Incorrect neighbor count returned for center.')

if __name__ == '__main__':
    unittest.main()