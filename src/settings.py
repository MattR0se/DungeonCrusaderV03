'''
global game settings
'''

from pygame.locals import FULLSCREEN, RESIZABLE

DEBUG = False

# SCREEN AND GRAPHICS
# size of the application window (in pixels)
WINDOW_SCALE = 3
# default Tilesize
TILE_WIDTH = 16
TILE_HEIGHT = 16
# game screen size in tiles
GAME_SCREEN_TILES_WIDE = 16
GAME_SCREEN_TILES_HIGH = 12
# GUI dimensions
GUI_MARGIN = 1
GUI_HEIGHT = TILE_HEIGHT * 3
# calculate game screen size (original pixel size)
GAME_SCREEN_W = TILE_WIDTH * GAME_SCREEN_TILES_WIDE  # should be 256
GAME_SCREEN_H = TILE_HEIGHT * GAME_SCREEN_TILES_HIGH + GUI_HEIGHT  # should be 240
# scale game screen to actual window size
WINDOW_W = GAME_SCREEN_W * WINDOW_SCALE
WINDOW_H = GAME_SCREEN_H * WINDOW_SCALE

print(GAME_SCREEN_W, GAME_SCREEN_H)

WINDOW_FLAGS = [
    RESIZABLE,
    #FULLSCREEN
    ]
    
# whether the game screen gets resized to the same aspect ratio as the window 
WINDOW_STRETCHED = False 

# Frames per second
FPS = 30

DEFAULT_FONT = 'Arial'

# MUSIC
# global volumes
MUSIC_VOLUME = 0.5
SFX_VOLUME = 0.6


# ingame settings
SCROLLSPEED_MENU = 12 #TODO: make this dt dependent

# player stats
PLAYER_HP_START = 14.0
PLAYER_MAX_HP = 14.0
PLAYER_HP_ROW = 7 # hearts per row

PLAYER_HITBOX_SIZE = (13, 8)
PLAYER_HITBOX_SIZE = (16, 8)
