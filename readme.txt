################
# Introduction #####################################################################
################

This is a template to show how to do basic things in pygame like draw shapes to the screen
at particular positions, create a moveable character, process input, and create a tile-based
system that can eventually be used for procedural generation, pathfinding, collision detection, etc.

The tile map is not fully implemented yet - when I'm done with it, the integer in each index
of the list will tell the renderer what to draw and where on every frame.

My plan going forward is to make a system like this that has the following functionality:

1. procedurally generate a dungeon for each level that connects with corridors and doorways and contain
different types of tiles

2. finish the tile map logic

3. implement a pathfinding system that moves the player from their current position
   to the position of the position they click along the most optimal path
   (I was thinking free movement when out of combat and then when you enter an enemy's line
    of sight it enters combat and switches to turn-based mode, but we can discuss this)

4. create algorithm to randomly place enemies, loot, locked doors, keys, an exit, etc. in each dungeon level.
   when you reach the exit, the current dungeon is serialized into binary and stored in save file so that
   you can return to previously-cleared dungeons as needed, and generates the next dungeon

5. implement tile-based collision detection system

###########################################################################################

We only need 1 main pygame file that contains the game loop to run the game, so all other files
can be eventually organized into other files in distinct modules, like maybe a file for handling
collision detection, a file for the class/leveling system, a file for map generation, a file for UI, etc.
and then the main program can simply import all those and use them

#######################
# Instructions to run #####################################################################
#######################

1. Simply install pygame-ce on your system (not pygame)
2. Then all you need to do is import pygame at the top of the main file and you can run them
   like any other python program