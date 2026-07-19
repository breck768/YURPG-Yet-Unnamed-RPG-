from node import Node

"""
DUNGEON GENERATOR CLASS (Work in Progress)

The dungeon is created by first performing binary space partitioning to construct
a tree where the leaf nodes end up being the rooms of the dungeon. After building the
tree, the nodes are traversed and the dungeon tile map is updated so that all floor
tiles have value of 0 and all wall tiles have value of 1

The goal for each dungeon is to find the portal/stairs/whatever we decide on that
takes you to the next level. When proceeding to a new level, the current dungeon map
is serialized and stored in the player's save file, the game is saved, and a new
dungeon is generated that is 1 level higher than the previous one.

TODO:
- Shrink rooms and create corridors + doorway tiles connecting them
- Implement new types of tiles such
- Make generated tile maps much larger and move around to move viewable area around
  the map
"""

class DungeonGenerator:
    def __init__(self, cell_size, map_width, map_height):
        self.root = None
        self.map_width = map_width
        self.map_height = map_height
        self.room_count =  10
        self.min_cell_size = 4
        self.dungeon = []

    def generateDungeon(self):
        rooms = 1
        self.refreshDungeon()
        while rooms < self.room_count:
            if self.root.divideCell(self.min_cell_size):
                rooms += 1
        self.updateTiles(self.root)
        return self.dungeon

    def updateTiles(self, node):
        if node.left is None and node.right is None:
            for y in range(node.y, node.y2):
                for x in range(node.x, node.x2):
                    if x == node.x or x == node.x2-1 or y == node.y or y == node.y2-1:
                        tile_type = 1
                    else:
                        tile_type = 0
                    self.dungeon[y * self.map_width + x] = tile_type

        if node.left:
            self.updateTiles(node.left)

        if node.right:
            self.updateTiles(node.right)

    def refreshDungeon(self):
        self.root = Node(1, 1, self.map_width-1, self.map_height-1)
        self.dungeon = [-1] * (self.map_width * self.map_height)