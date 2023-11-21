class GameMap:
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)] # Cardinal directions

    def __init__(self, width=64, height=32):
        self.width = width if width > 0 else 1
        self.height = height if width > 0 else 1

    def get_neighbors(self, x, y):
        '''Gets neighbor cells in cardinal directions.'''
        
        res = []
        for dir in self.dirs:
            neighbor = (x + dir[0], y + dir[1])

            # Only add cells within the map boundary
            if 0 <= neighbor[0] < self.width and 0 <= neighbor[1] < self.height:
                res.append(neighbor)
        return res