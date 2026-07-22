import pygame

"""
Accepts a list of integers representing the tiles to render and
converts world coordinates to viewport coordinates to allow only
a viewport-sized section of the map centered on the player to be drawn
to the screen on each frame
"""

def renderTilemap(dungeon, viewport_w, viewport_h, tile_size, surface):
    player = dungeon.player_tile
    map = dungeon.tiles
    width = dungeon.map_width
    vp_start_col = max(0, (player % width) - (viewport_w // 2))
    vp_start_row = max(0, (player // width) - (viewport_h // 2))
    vp_end_col = min(width, vp_start_col + viewport_w)
    vp_end_row = min(dungeon.map_height, vp_start_row + viewport_h)
    if vp_end_col - vp_start_col < viewport_w:
        vp_start_col = vp_end_col - viewport_w
    if vp_end_row - vp_start_row < viewport_h:
        vp_start_row = vp_end_row - viewport_h

    # Convert each tile from world space to viewport space and draw to screen
    for row in range(vp_start_row, vp_end_row):
        for col in range(vp_start_col, vp_end_col):
            i = row * width + col
            x = (col * tile_size) - (vp_start_col * tile_size)
            y = (row * tile_size) - (vp_start_row * tile_size)
            if i == player:
                color = (0, 0, 255)
            elif map[i] == 0:
                color = (0, 50, 0)
            elif map[i] == 1:
                color = (255, 255, 255)
            elif map[i] == 2:
                color = (139, 69, 19)
            else:
                color = (0, 0, 0)
            pygame.draw.rect(surface, color, pygame.Rect(x, y, tile_size, tile_size))
    return vp_start_row * width + vp_start_col