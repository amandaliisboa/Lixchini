import pygame

# C
COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (178, 34, 34)
COLOR_YELLOW = (201, 162, 39)
COLOR_PINK = (255, 105, 180)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'sky0': 0,
    'sky1': 1,
    'sky2': 2,
    'sky3': 3,
    'sky4': 4,
    'sky5': 5,
    'sky6': 6,
    'Player1': 3,
    'Player1Shot': 1,
    'Player2': 3,
    'Player2Shot': 3,
    'enemy1': 1,
    'enemy1Shot': 5,
    'enemy2': 1,
    'enemy2Shot': 2,
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

#S
SPAWN_TIME = 4000
# w
WIN_WIDTH = 700
WIN_HEIGHT = 500

# S
ENTITY_SCALE = {
    'sky0': 1, 'sky1': 1, 'sky2': 1, 'sky3': 1,
    'sky4': 1, 'sky5': 1, 'sky6': 1,
    'Player1': 0.2,
    'Player2': 0.2,
    'enemy1': 1,
    'enemy2': 1,
}

# H

ENTITY_HEALTH = {
    'sky0': 999,
    'sky1': 999,
    'sky2': 999,
    'sky3': 999,
    'sky4': 999,
    'sky5': 999,
    'sky6': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'enemy1': 50,
    'enemy1Shot': 1,
    'enemy2': 60,
    'enemy2Shot': 1,
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 15,
    'enemy1': 100,
    'enemy2': 200,
}