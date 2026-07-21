from node import Node
import random

"""
TODO:
- Implement doorway, enemy, key, and portal tiles
- Make generated tile maps larger
- Implement local/world map scaling
"""

class Dungeon:
    def __init__(self, cell_size, map_width, map_height):
        self.root = None
        self.cell_size = cell_size
        self.map_width = map_width
        self.map_height = map_height
        self.total_rooms =  20
        self.min_cell_size = 10
        self.rooms = None
        self.tiles = None
        self.player_pos = None

    def shrinkRooms(self):
        self.root.shrink(self.min_cell_size)

    def findNeighbors(self):
        self.root.getRooms(self.rooms)
        for room_A in self.rooms:
            for room_B in self.rooms:
                if room_A != room_B:
                    if room_A.x2 == room_B.x1:
                        if max(room_A.y1, room_B.y1) < min(room_A.y2, room_B.y2):
                            room_A.h_neighbors.append(room_B)
                    if room_A.y2 == room_B.y1:
                        if max(room_A.x1, room_B.x1) < min(room_A.x2, room_B.x2):
                            room_A.v_neighbors.append(room_B)

    def createHCorridor(self, x1, x2, y):
        for x in range(x1, x2):
            self.tiles[y * self.map_width + x] = 3

    def createVCorridor(self, y1, y2, x):
        for y in range(y1, y2):
            self.tiles[y * self.map_width + x] = 3

    def generateDungeon(self):
        cur_room_count = 1
        self.refreshDungeon()
        while cur_room_count < self.total_rooms:
            if self.root.divideCell(self.min_cell_size):
                cur_room_count += 1
        self.findNeighbors()
        # set doorway tiles here before shrinking
        self.shrinkRooms()
        self.updateTiles(self.root)
        self.placePlayer()
        return self.tiles

    def placePlayer(self):
        start_room = self.rooms[random.randint(1, self.total_rooms-1)]
        start_col = random.randint(start_room.x1 + 2, start_room.x2 - 2)
        start_row = random.randint(start_room.y1 + 2, start_room.y2 - 2)
        starting_tile = start_row * self.map_width + start_col
        self.tiles[starting_tile] = 4
        self.player_pos = [starting_tile // self.map_width, starting_tile % self.map_width]

    def updateTiles(self, node):
        for room in self.rooms:
            for y in range(room.y1, room.y2):
                for x in range(room.x1, room.x2):
                    if x == room.x1 or x == room.x2-1 or y == room.y1 or y == room.y2-1:
                        tile_type = 1
                    else:
                        tile_type = 0
                    self.tiles[y * self.map_width + x] = tile_type
            for neighbor in room.h_neighbors:
                min_y2 = min(room.y2, neighbor.y2)
                max_y1 = max(room.y1, neighbor.y1)
                if min_y2 - max_y1 >= self.cell_size:
                    cy = random.randint(max_y1+1, (min_y2-1) - 1)
                    self.createHCorridor(room.x2, neighbor.x1, cy)
            for neighbor in room.v_neighbors:
                min_x2 = min(room.x2, neighbor.x2)
                max_x1 = max(room.x1, neighbor.x1)
                if min_x2 - max_x1 >= self.cell_size:
                    cx = random.randint(max_x1+1, (min_x2-1) - 1)
                    self.createVCorridor(room.y2, neighbor.y1, cx)

    def refreshDungeon(self):
        self.root = Node(1, 1, self.map_width-1, self.map_height-1)
        self.rooms = []
        self.tiles = [-1] * (self.map_width * self.map_height)