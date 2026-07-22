import pygame
import sys
import pathfinding
import renderer
from dungeon import Dungeon

# This script launches the game.

"""
TODO:
- Make distinct player entity separate from dungeon and implement smooth inter-tile movement.
  Also make the renderer draw player separately
- Make 2 rendering modes - world map and viewport map - open world map by pressing 'm'
- Implement player visibility radius. Any tiles blocked by wall or
  outside visibility radius are black out
- Implement algorithm for spawning enemies, items, and portal to reach next dungeon
- Finish implementing state logic
"""

### Constants ###
WIN_WIDTH = 1280                                                # Screen resolution width
WIN_HEIGHT = 720                                                # Screen resolution height
TILE_SIZE = 16                                                  # Width/height of each tile

# Game states
EXPLORATION_STATE = 0
COMBAT_STATE = 1
MENU_STATE = 2
MOVING_STATE = 3

### Controls (edit once menus are done) ###
# Click mouse to move
# Press q to quit

# Initialization
pygame.init()
viewport_cols = WIN_WIDTH // TILE_SIZE                          # viewport horizontal tile count
viewport_rows = WIN_HEIGHT // TILE_SIZE                         # viewport vertical tile count
dungeon_cols = viewport_cols * 5                                # dungeon horizontal tile count
dungeon_rows = viewport_rows * 5                                # dungeon vertical tile count
game_state = EXPLORATION_STATE                                  # game state dictates what happens in game loop
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))       # surface to draw graphics to
clock = pygame.time.Clock()                                     # game clock

# Variables used to track player movement
move_start_time = 0
move_elapsed_time = 0
move_path_nodes = None
move_path = None
move_step_count = 0
move_dest = None

# Procedurally generate a dungeon using binary spatial partitioning
dungeon = Dungeon(TILE_SIZE, dungeon_cols, dungeon_rows)

# Game loop
run = True
while run:
    # On each frame, clear and redraw the screen
    screen.fill((0,0,0))
    vp_pos = renderer.renderTilemap(dungeon, viewport_cols, viewport_rows, TILE_SIZE, screen)

    # Display start menu on launch:
        # NEW GAME
        # LOAD GAME
        # HOW TO PLAY
        # QUIT

    # On new game, open character creation/class selection menu

    # Once character has been created, generate a level dungeon and place
    # player/enemies/items

    # Once in game, need logic for the following states:
        # EXPLORATION   - done
        # MOVING        - done
        # COMBAT
        # MENU

    # If game is loaded, read data from save file, deserialize it,
    # and draw the tile map as it was when saved.

    # Create instructions page

    # Change 'q' to quit to the QUIT button in main/pause menus

    # Controls for exploration state
    if game_state == EXPLORATION_STATE:
        for e in pygame.event.get():
            # on quit
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_q:
                    run = False
                    pygame.quit()
                    sys.exit()
            # Get clicked tile using click event position and
            # pass it to pathfinder
            if e.type == pygame.MOUSEBUTTONDOWN:
                viewport_col = vp_pos % dungeon_cols
                viewport_row = vp_pos // dungeon_cols
                dest_col = (int(e.pos[0]) // TILE_SIZE) + viewport_col
                dest_row = (int(e.pos[1]) // TILE_SIZE) + viewport_row
                move_dest = dest_row * dungeon_cols + dest_col
                if dungeon.tiles[move_dest] == 0 or dungeon.tiles[move_dest] == 2:
                    move_path_nodes = pathfinding.findPath(dungeon, move_dest)
                    cur = move_dest
                    move_path = [cur]
                    while cur != dungeon.player_tile:
                        cur = move_path_nodes[cur][3]
                        move_path.insert(0, cur)
                    move_step_count = 0
                    game_state = MOVING_STATE
                    move_start_time = pygame.time.get_ticks()

    # If moving, make a step along the movement path every 2 milliseconds until destination tile is reached
    elif game_state == MOVING_STATE:
        if move_step_count < len(move_path):
            if pygame.time.get_ticks() - move_start_time > 25:
                dungeon.player_tile = move_path[move_step_count]
                move_step_count += 1
                move_start_time = pygame.time.get_ticks()
        else:
            game_state = EXPLORATION_STATE

    pygame.display.flip()
    clock.tick(60)