import pygame

# C
COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (178, 34, 34)
COLOR_YELLOW = (201, 162, 39)

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
    'Player2': 3,
    'enemy1': 2,
    'enemy2': 2,
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
WIN_WIDTH = 900
WIN_HEIGHT = 550

# S
ENTITY_SCALE = {
    'sky0': 1, 'sky1': 1, 'sky2': 1, 'sky3': 1,
    'sky4': 1, 'sky5': 1, 'sky6': 1,
    'Player1': 1.5,
    'Player2': 1.5,
    'enemy1': 1.5,
    'enemy2': 1.5,
}