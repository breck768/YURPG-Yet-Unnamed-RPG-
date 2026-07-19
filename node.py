import random

"""
DUNGEON NODE CLASS

Node objects represent rooms in dungeons and are used to construct a binary tree
for the binary search partitioning algorithm. The root dungeon node is subdivided
recursively until it meets minimum constraints, after which it becomes a leaf node
in the binary tree. Each leaf nodeof the tree represents a room in the dungeon.
"""

class Node:
    def __init__(self, x, y, x2, y2):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.left = None
        self.right = None

    def divideCell(self, min_size):
        width = self.x2-self.x
        height = self.y2-self.y
        if width < min_size or height < min_size:
            return False
        if self.left != None:
            if random.randint(1, 100) < 50:
                return self.left.divideCell(min_size)
            else:
                return self.right.divideCell(min_size)
        if width > height:
            midpoint = int(self.x + random.uniform(0.3, 0.6) * width)
            self.left = Node(self.x, self.y, midpoint, self.y2)
            self.right = Node(midpoint, self.y, self.x2, self.y2)
            return True
        else:
            midpoint = int(self.y + random.uniform(0.3, 0.6) * height)
            self.left = Node(self.x, self.y, self.x2, midpoint)
            self.right = Node(self.x, midpoint, self.x2, self.y2)
            return True

    