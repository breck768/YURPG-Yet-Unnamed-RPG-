"""
Use A* algorithm to calculate shortest path between start and dest tiles.
Outputs a dictionary called 'node-map' that contains all tiles that were traversed.
Each value in the dict has a parent that allows the path to be traversed.
"""

def findPath(tilemap, dest):
    start = tilemap.player_tile
    width = tilemap.map_width
    open_set = {start}
    node_map = {}
    node_map[start] = [0, 0, 0, None]
    closed_set = set()
    map_size = len(tilemap.tiles)
    
    while open_set:
        cur = min(open_set, key=lambda tile: node_map[tile][2])
        open_set.remove(cur)
        closed_set.add(cur)
        
        if cur == dest:
            return node_map
        
        neighbors = [
            cur - 1,       # left
            cur + 1,       # right
            cur - width,   # up
            cur + width    # down
        ]

        for n in neighbors:
            if tilemap.tiles[n] == 0 or tilemap.tiles[n] == 2:
                if 0 <= n < map_size and n not in closed_set:
                    g = node_map[cur][0] + 1
                    if n not in open_set or g < node_map[n][0]:
                        open_set.add(n)
                        h = abs(n%width - dest%width) + abs(n//width - dest//width)
                        node_map[n] = [g, h, g+h, cur]