import pygame

# cores usadas no jogo
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (178, 34, 34)
COLOR_PINK = (255, 105, 180)
COLOR_GREEN = (0, 128, 0)
COLOR_BLUE = (0, 0, 255)

# eventos customizados do pygame
EVENT_ENEMY = pygame.USEREVENT + 1    # spawn de inimigo
EVENT_TIMEOUT = pygame.USEREVENT + 2  # contagem regressiva do level

# velocidade de movimento de cada entidade (pixels por frame)
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
    'Player1': 3,
    'Player1Shot': 1,
    'Player2': 3,
    'Player2Shot': 3,
    'enemy1': 1,
    'enemy1Shot': 3,
    'enemy2': 1,
    'enemy2Shot': 4,
}

# opções do menu principal
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# teclas de movimento de cada player
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

# tempo em ms entre cada spawn de inimigo
SPAWN_TIME = 2000

# controle do timeout do level
TIMEOUT_STEP = 100       # quanto diminui a cada tick
TIMEOUT_LEVEL = 20000    # tempo total do level em ms

# tamanho da janela
WIN_WIDTH = 700
WIN_HEIGHT = 500

# posições dos textos na tela de score
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 150),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 200),
             1: (WIN_WIDTH / 2, 220),
             2: (WIN_WIDTH / 2, 240),
             3: (WIN_WIDTH / 2, 260),
             4: (WIN_WIDTH / 2, 280),
             5: (WIN_WIDTH / 2, 300),
             6: (WIN_WIDTH / 2, 320),
             7: (WIN_WIDTH / 2, 340),
             8: (WIN_WIDTH / 2, 360),
             9: (WIN_WIDTH / 2, 380),
             }

# escala de cada entidade na tela
ENTITY_SCALE = {
    'Level1Bg0': 1, 'Level1Bg1': 1, 'Level1Bg2': 1, 'Level1Bg3': 1,
    'Level1Bg4': 1, 'Level1Bg5': 1, 'Level1Bg6': 1,
    'Player1': 0.2,
    'Player2': 0.2,
    'enemy1': 1,
    'enemy2': 1,
}

# vida inicial de cada entidade
ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Player1': 500,
    'Player1Shot': 1,
    'Player2': 500,
    'Player2Shot': 1,
    'enemy1': 30,
    'enemy1Shot': 1,
    'enemy2': 20,
    'enemy2Shot': 1,
}

# frames de espera entre cada tiro
ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 15,
    'enemy1': 40,
    'enemy2': 60,
}

# dano causado por cada entidade ao colidir
ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 20,
    'enemy1': 1,
    'enemy1Shot': 20,
    'enemy2': 1,
    'enemy2Shot': 20,
}

# pontos ganhos ao destruir cada entidade
ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'enemy1': 100,
    'enemy1Shot': 0,
    'enemy2': 125,
    'enemy2Shot': 0,
}