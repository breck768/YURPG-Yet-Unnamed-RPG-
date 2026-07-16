import pygame
import sys

### Basic pygame demo ###

# See readme for instructions to run, details, and ideas for plans going forward

### Controls ###
# Press arrow keys to move
# Press q to quit

pygame.init()
W, H = 640, 480        # window size
tile_size = 32          # tile size
rows = W // tile_size   # tile map rows
cols = H // tile_size   # tile map cols
speed = 4               # distance moved per frame

pygame.display.set_caption("Pygame Starter Demo")
screen = pygame.display.set_mode((W, H))            # foreground surface to draw objects that move
background = pygame.Surface((W, H))                 # background surface to draw stationary objects

# Tile map - a list of integers, where each integer stands for a different type of tile.
# When drawing the screen (in the final version), the renderer will use the number in each index
# of the tile map to know what type of object to draw (player, enemy, wall, door, chest, loot, etc.)
# Used for rendering objects, collision detection, pathfinding, procedural generation, etc.
tile_map = [0] * (rows * cols)

# Game timer
clock = pygame.time.Clock()

# Player example
player = pygame.Rect(W // 2 - tile_size, H // 2 - tile_size//2, tile_size, tile_size)

# Example of walls around perimeter of screen
# Tilemap is a 1D list because it has faster iteration
# See below for how to calculate x,y position for tiles from 1D list
for i, tile in enumerate(tile_map):
    x = i % rows
    y = i // rows
    if x == 0 or x == rows-1 or y == 0 or y == cols-1:
        pygame.draw.rect(background, (255, 255, 255), pygame.Rect(x*tile_size, y*tile_size, tile_size, tile_size))
    else:
        pygame.draw.rect(background, (255, 255, 255), pygame.Rect(x*tile_size, y*tile_size, tile_size, tile_size), 1)

# Game loop
run = True
while run:
    screen.fill((0,0,0))                                # each frame screen is cleared/redrawn
    screen.blit(background, (0, 0))                     # draw static background
    pygame.draw.rect(screen, (255, 0, 0), player)       # draw updated player position

    # Event handling
    for e in pygame.event.get():
        # on quit
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_q:
                 pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > tile_size:
        player.move_ip(-speed, 0)
    if keys[pygame.K_RIGHT] and player.right < W - tile_size:
        player.move_ip(speed, 0)
    if keys[pygame.K_UP] and player.top > tile_size:
        player.move_ip(0, -speed)
    if keys[pygame.K_DOWN] and player.bottom < H - tile_size:
        player.move_ip(0, speed)

    pygame.display.flip()
    clock.tick(60)