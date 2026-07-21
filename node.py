import random

class Node:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.width = x2 - x1
        self.height = y2 - y1
        self.left = None
        self.right = None
        self.h_neighbors = []
        self.v_neighbors = []
        self.h_halls = []
        self.v_halls = []

    def shrink(self, min_size):
        if self.left == None:
            new_width = int(max(self.width * random.uniform(0.6, 0.9), min_size))
            new_height = int(max(self.height * random.uniform(0.6, 0.9), min_size))
            self.x1 = int(self.x1 + 0.5*(self.width - new_width))
            self.x2 = int(self.x2 - 0.5*(self.width - new_width))
            self.y1 = int(self.y1 + 0.5*(self.height - new_height))
            self.y2 = int(self.y2 - 0.5*(self.height - new_height))
            self.width = new_width
            self.height = new_height
        else:
            self.left.shrink(min_size)
            self.right.shrink(min_size)

    def getRooms(self, nodes):
        if self.left == None:
            nodes.append(self)
        else:
            self.left.getRooms(nodes)
            self.right.getRooms(nodes)

    def divideCell(self, min_size):
        if self.width < min_size or self.height < min_size:
            return False
        if self.left != None:
            if random.randint(1, 100) < 50:
                return self.left.divideCell(min_size)
            else:
                return self.right.divideCell(min_size)
        if self.width > self.height:
            midpoint = int(self.x1 + random.uniform(0.3, 0.6) * self.width)
            self.left = Node(self.x1, self.y1, midpoint, self.y2)
            self.right = Node(midpoint, self.y1, self.x2, self.y2)
            return True
        else:
            midpoint = int(self.y1 + random.uniform(0.3, 0.6) * self.height)
            self.left = Node(self.x1, self.y1, self.x2, midpoint)
            self.right = Node(self.x1, midpoint, self.x2, self.y2)
            return True