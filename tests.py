import dungeon_generator as dungen
import unittest

class TestGameMap(unittest.TestCase):
    def test_width(self):
        width = 10
        map = dungen.GameMap(width, 20)
        self.assertEqual(map.width, width, 'The map did not correctly set its width.')
    
    def test_height(self):
        height = 20
        map = dungen.GameMap(10, height)
        self.assertEqual(map.height, height, 'The map did not correctly set its height.')

if __name__ == '__main__':
    unittest.main()