import pygame
import sys
from dungeon import Dungeon

# This script launches the game.

"""
TODO:
- Create renderer module that uses viewport-sized camera with player at the center
  to move around the dungeon. Need to render only tiles in range of camera by
  converting their world space coordinates to viewport space.
- Implement player visibility using raycasting. Any tiles blocked by wall or
  outside visibility radius are black out
- Implement pathfinding module
- Implement algorithm for spawning enemies, items, and portal to reach next dungeon
- Implement state machine that determines what can happen in game loop
  depending on game state
  (MENU, EXPLORE, COMBAT, etc)
"""

### Constants ###
WIN_WIDTH = 1024
WIN_HEIGHT = 768
TILE_SIZE = 4

### Controls ###
# Press q to quit

# Move this into renderer module and change so that it takes world tile data as
# input and renders only tiles in the viewport by converting world space coordinates
# to viewport space
def renderGraphics(map):
    for i, tile in enumerate(map):
        x = i % viewport_cols
        y = i // viewport_cols
        if map[i] == 0:
            color = (0, 50, 0)
        elif map[i] == 1:
            color = (255, 255, 255)
        elif map[i] == 2:
            color = (139, 69, 19)
        elif map[i] == 3:
            color = (255, 255, 0)
        elif map[i] == 4:
            color = (0, 0, 255)
        else:
            color = (0, 0, 0)
        pygame.draw.rect(background, color, pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))


pygame.init()
viewport_cols = WIN_WIDTH // TILE_SIZE
viewport_rows = WIN_HEIGHT // TILE_SIZE
dungeon_cols = viewport_cols * 5
dungeon_rows = viewport_rows * 5
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))                    # foreground surface to draw objects that move
background = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))                         # background surface to draw stationary objects
clock = pygame.time.Clock()

# Dungeon generator test
dungeon = Dungeon(TILE_SIZE, viewport_cols, viewport_rows)
renderGraphics(dungeon.generateDungeon())

# Game loop
run = True
while run:
    screen.fill((0,0,0))                                # each frame screen is cleared/redrawn
    screen.blit(background, (0, 0))                     # draw static background

    # Display start menu on launch:
        # NEW GAME
        # LOAD GAME
        # HOW TO PLAY
        # QUIT

    # On new game, open character creation/class selection menu

    # Once character has been created, generate a level 1 dungeon and place
    # player/enemies/items

    # If game is loaded, read data from save file, deserialize it,
    # and draw the tile map as it was when saved.

    # ...

    # Controls - (change depending on game state)
    for e in pygame.event.get():
        # on quit
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_q:
                run = False
                pygame.quit()
                sys.exit()
            if e.key == pygame.K_g:
                renderGraphics(dungeon.generateDungeon())

    pygame.display.flip()
    clock.tick(60)