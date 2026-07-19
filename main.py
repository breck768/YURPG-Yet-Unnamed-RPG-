import pygame
import sys
from dungeon import DungeonGenerator

# This script launches the game.

"""
TODO:
- Create camera with player at center that moves viewable window around
  a larger map
- Create visibility radius around player - any tiles outside the radius are black
  out
- Implement pathfinding module
- Implement algorithm for spawning enemies
- Implement dungeon levels, where higher the level == stronger the enemies and more
  difficult dungeon
"""

### Controls ###
# Press q to quit

# Generate new dungeon
def renderGraphics(map):
    for i, tile in enumerate(map):
        x = i % map_width
        y = i // map_width
        if map[i] == 1:
            color = (255, 255, 255)
        elif map[i] == 0:
            color = (0, 50, 0)
        else:
            color = (0, 0, 0)
        pygame.draw.rect(background, color, pygame.Rect(x*tile_size, y*tile_size, tile_size, tile_size))


pygame.init()
W, H = 1024, 768                                            # window resolution
tile_size = 8
map_width = W // tile_size                                  # window width in tiles
map_height = H // tile_size                                 # window height in tiles
pygame.display.set_caption("Dungeon Generator Prototype")
screen = pygame.display.set_mode((W, H))                    # foreground surface to draw objects that move
background = pygame.Surface((W, H))                         # background surface to draw stationary objects
clock = pygame.time.Clock()                                 # Frame timer

# Create dungeon generator (test)
dun_gen = DungeonGenerator(tile_size, map_width, map_height - 5)
renderGraphics(dun_gen.generateDungeon())

# Game loop
run = True
while run:
    screen.fill((0,0,0))                                # each frame screen is cleared/redrawn
    screen.blit(background, (0, 0))                     # draw static background

    # Instructions
    font = pygame.font.Font(None, tile_size*5)
    instr_box = pygame.Rect(0, H-tile_size*5, W, tile_size*5)
    instr = font.render("Press g to generate a new dungeon and q to quit.", True, (255, 0, 0))
    instr_rect = instr.get_rect(center=instr_box.center)
    screen.blit(instr, instr_rect)

    # Display start menu on launch:
        # NEW GAME
        # LOAD GAME
        # HOW TO PLAY
        # QUIT

    # On new game, open character creation/class selection menu

    # Once character has been created, generate a level 1 dungeon and place
    # player/enemies/items

    # ...

    # Controls
    for e in pygame.event.get():
        # on quit
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_q:
                run = False
                pygame.quit()
                sys.exit()
            if e.key == pygame.K_g:
                renderGraphics(dun_gen.generateDungeon())

    pygame.display.flip()
    clock.tick(60)