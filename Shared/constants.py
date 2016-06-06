__author__ = 'user'

# 10*16

BLOCKSIZE = 20
BLOCKS_H = 10
BLOCKS_V = 16
BLOCKS_V = 20
# NEXT_H = 4
# NEXT_V = 4
NEXT_OFFSET = 2
NEXT_LEVEL_LINES = 20

SPACER = 3

P_TEXT_COLOR = (255, 0, 0)
P_BG_COLOR = (10, 10, 10)

GO_TEXT_COLOR = (255, 0, 0)
GO_BG_COLOR = (10, 10, 10)

TEXT_COLOR = (255, 0, 0)
BG_COLOR = (10, 10, 10)
# EMPTY_CELL_COLOR =
COLORS = [
    (25, 25, 25),  # grey
    (255, 0, 0),  #red
    (0, 255, 0),  #green
    (0, 0, 255),  #blue
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255),
    (255, 128, 0),
    (128, 0, 255),
    (0, 128, 255),

]
# print(len(COLORS))
COLORS_COUNT = len(COLORS)

CLASSIC_FIGURE_SIZE = 4
CLASSIC_FIGURES = [
    [[1, 1, ],  # Г1
     [1, 0, ],
     [1, 0, ]],

    [[1, 1, ],  # Г2
     [0, 1, ],
     [0, 1, ]],

    [[1, 1],  # Кубик
     [1, 1]],

    [[1, 0],  # Смещённая 1
     [1, 1, ],
     [0, 1]],

    [[0, 1],  # Смещённая 2
     [1, 1],
     [1, 0]],

    [[1, 0],  # T-образная
     [1, 1],
     [1, 0]],

    [[1],  # Палка
     [1],
     [1],
     [1]]
]

PENTAMINO_FIGURE_SIZE = 5
PENTAMINO_FIGURES = [
    [[0,1,1],
     [1,1,0],
     [0,1,0]],

    [[1],[1],[1],[1],[1]],

    [[1,0],
     [1,0],
     [1,0],
     [1,1]],

    [[0,1],
     [0,1],
     [1,1],
     [1,0]],

    [[1,1],
     [1,1],
     [1,0]],

    [[1,1,1],
     [0,1,0],
     [0,1,0]],

    [[1,0,1],
     [1,1,1]],

    [[0,0,1],
     [0,0,1],
     [1,1,1]],

    [[0,0,1],
     [0,1,1],
     [1,1,0]],

    [[0,1,0],
     [1,1,1],
     [0,1,0]],

    [[0,1],
     [1,1],
     [0,1],
     [0,1]],

    [[1,1,0],
     [0,1,0],
     [0,1,1]]
]

# FIGURES = CLASSIC_FIGURES
NEXT_H = 5
NEXT_V = 5
# FIGURES = PENTAMINO_FIGURES
FIGURES = CLASSIC_FIGURES

FIGURES_COUNT = len(FIGURES)

def calculate_screen_size(BLOCKS_H_IN, BLOCKS_V_IN ):
    return [(SPACER + BLOCKSIZE) * (BLOCKS_H_IN + NEXT_OFFSET * 2 + NEXT_H) + SPACER,
               (SPACER + BLOCKSIZE) * BLOCKS_V_IN + SPACER]

SCREEN_SIZE = calculate_screen_size(BLOCKS_H, BLOCKS_V)

PLAYING_SCENE = 0
GAMEOVER_SCENE = 1
PAUSE_SCENE = 2
MENU_SCENE = 3
HIGHSCORE_SCENE = 4

FONTNAME = "Arial"
FONTNAME_COUR = "Courier"
FONTSIZE = 32


KEYBOARD_REPEAT = (200, 25)

#speed
pyTimer = 50 #200
maxTicks = 50 #100
levelMultiplier = 20

