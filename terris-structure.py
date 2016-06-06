__author__ = 'user'

import pygame
import constants
import logic_structure
import render_structure
import random
import copy
# from Scenes import GameScene
# from Scenes import *

__lives = 1
__score = 0
__level = 1  # Level
__destroyed = 0
__lines = 0
__figures = 0
__desk = logic_structure.create_desk(constants.BLOCKS_V, constants.BLOCKS_H)
__desk_next = logic_structure.create_desk(constants.NEXT_V, constants.NEXT_H)
__gamePaused = False
__gameOver = False
__figure = copy.deepcopy(constants.FIGURES[random.randint(0,constants.FIGURES_COUNT-1)])
__figure = logic_structure.set_figure_colour(__figure.copy())
__figures += 1
__fig_pos = [0, int(constants.BLOCKS_H / 2 - len(__figure[0]) / 2)]
__figure_next = copy.deepcopy(constants.FIGURES[random.randint(0,constants.FIGURES_COUNT-1)])  # random.randint(0,constants.FIGURES_COUNT-1)])
__figure_next = logic_structure.set_figure_colour(__figure_next.copy())

pygame.init()
pygame.mixer.init()
pygame.display.set_caption(
    "TetrisStr - Score:" + str(__score) + " Level:" + str(__level) + " Lines:" + str(__lines) + " Figures:" + str(
        __figures) + " Bricks:" + str(__destroyed))

__clock = pygame.time.Clock()
tick = 1

screen = pygame.display.set_mode(constants.SCREEN_SIZE, pygame.DOUBLEBUF, 32)

pygame.mouse.set_visible(1)
pygame.key.set_repeat(constants.KEYBOARD_REPEAT[0],constants.KEYBOARD_REPEAT[1])

# scene = Scene(self)

while 1:
    screen.fill(constants.BG_COLOR)

    __clock.tick(constants.pyTimer + (__level - 1) * constants.levelMultiplier)
    events = pygame.event.get()
    mods = pygame.key.get_mods()

    for event in events:
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN and __gamePaused:
            __gamePaused = False
            pygame.key.set_repeat(constants.KEYBOARD_REPEAT[0],constants.KEYBOARD_REPEAT[1])

        if event.type == pygame.KEYDOWN and __gameOver:
            __lives = 1
            __score = 0
            __level = 1  # Level
            __destroyed = 0
            __lines = 0
            __figures = 0
            __desk = logic_structure.create_desk(constants.BLOCKS_V, constants.BLOCKS_H)
            __gameOver = False
            __figure = copy.deepcopy(constants.FIGURES[random.randint(0, constants.FIGURES_COUNT - 1)])
            __figure = logic_structure.set_figure_colour(__figure.copy())
            __figures += 1
            __fig_pos = [0, int(constants.BLOCKS_H / 2 - len(__figure[0]) / 2)]
            __figure_next = copy.deepcopy(constants.FIGURES[6])  # random.randint(0,constants.FIGURES_COUNT-1)])
            __figure_next = logic_structure.set_figure_colour(__figure_next.copy())
            pygame.key.set_repeat(250, 25)

        if event.type == pygame.KEYDOWN  and not __gameOver:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                exit()

            if event.key == pygame.K_p:
                __gamePaused = True
                pygame.key.set_repeat(0, 0)

            if event.key == pygame.K_RIGHT and mods ==64:
                constants.BLOCKS_H +=1
                for y in range(len(__desk)): __desk[y].append(0)

            if event.key == pygame.K_LEFT and mods ==64 and constants.BLOCKS_H>5:
                constants.BLOCKS_H -=1
                for y in range(len(__desk)): __desk[y].pop()
                if __fig_pos[1]+len(__figure[0])>len(__desk[0]):
                    __fig_pos[1] -=1

            if event.key == pygame.K_DOWN and mods ==64:
                constants.BLOCKS_V +=1
                __desk = logic_structure.add_empty_line(copy.deepcopy(__desk))

            if event.key == pygame.K_UP and mods ==64 and constants.BLOCKS_V>5:
                constants.BLOCKS_V -=1
                __desk.pop()

            if (event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and mods ==64:
                constants.SCREEN_SIZE = constants.calculate_screen_size(constants.BLOCKS_H, constants.BLOCKS_V)
                screen = pygame.display.set_mode(constants.SCREEN_SIZE, pygame.DOUBLEBUF, 32)

            if (event.key == pygame.K_RIGHT or event.key == pygame.K_KP6) and mods == 0:
                if not logic_structure.check_intersect(__desk, __figure, [__fig_pos[0], __fig_pos[1] + 1]):
                    __fig_pos[1] += 1

            if (event.key == pygame.K_LEFT or event.key == pygame.K_KP4)  and mods == 0:
                if not logic_structure.check_intersect(__desk, __figure, [__fig_pos[0], __fig_pos[1] - 1]):
                    __fig_pos[1] -= 1

            if (event.key == pygame.K_5 or event.key == pygame.K_UP or event.key == pygame.K_KP5) and mods == 0:
                tmp_rotated, tmp_pos = logic_structure.rotate(__figure, __fig_pos)
                if len(tmp_rotated[0]) + tmp_pos[1] >= len(__desk[0]): #len(__figure[0]) + __fig_pos[1] == len(__desk[0]): # trying to move on -1 from right
                    tmp_pos[1] -= (len(tmp_rotated[0]) + tmp_pos[1]) - len(__desk[0])
                    # print("Fuck")
                if tmp_pos[1] <0: #__fig_pos[1] == 0:  # tryin to move on +1 from left
                    tmp_pos[1] = 0

                if not logic_structure.check_intersect(__desk, tmp_rotated, tmp_pos):  # simple turn on an empty space
                    __figure, __fig_pos = tmp_rotated, tmp_pos # logic_structure.rotate(__figure, __fig_pos)

                """if len(tmp_rotated[0]) + tmp_pos[1] >= len(__desk[0]): #len(__figure[0]) + __fig_pos[1] == len(__desk[0]): # trying to move on -1 from right
                    tmp_pos[1] -= (len(tmp_rotated[0]) + tmp_pos[1]) - len(__desk[0])
                    # tmp_rotated, tmp_pos = logic_structure.rotate(__figure, [__fig_pos[0], __fig_pos[1] - 1])
                    if not logic_structure.check_intersect(__desk, tmp_rotated, tmp_pos):
                        __figure, __fig_pos = tmp_rotated, tmp_pos #logic_structure.rotate(__figure, [__fig_pos[0], __fig_pos[1]])

                if tmp_pos[1] <0: #__fig_pos[1] == 0:  # tryin to move on +1 from left
                    tmp_pos[1] = 0
                    # tmp_rotated, tmp_pos = logic_structure.rotate(__figure, [__fig_pos[0], __fig_pos[1] + 1])
                    if not logic_structure.check_intersect(__desk, tmp_rotated, tmp_pos):
                        __figure, __fig_pos = tmp_rotated, tmp_pos # logic_structure.rotate(__figure, [__fig_pos[0], __fig_pos[1]])"""

            if (event.key == pygame.K_SPACE or event.key == pygame.K_DOWN or event.key == pygame.K_KP2) and mods == 0:
                if not logic_structure.check_intersect(__desk, __figure, [__fig_pos[0] + 1, __fig_pos[1]]):
                    __fig_pos[0] += 1
                else:
                    tick = constants.maxTicks - 1

            if (event.key == pygame.K_KP8) and mods == 0:
                if not logic_structure.check_intersect(__desk, __figure, [__fig_pos[0] - 1, __fig_pos[1]]):
                    __fig_pos[0] -= 1
                    if __fig_pos[0] <0 : __fig_pos[0]=0


    render_structure.render_desk(screen, __desk, 0, 0)
    render_structure.render_desk(screen, __desk_next,
                                 (constants.BLOCKS_H + constants.NEXT_OFFSET) * (constants.BLOCKSIZE + constants.SPACER),
                                 (constants.BLOCKSIZE + constants.SPACER))

    render_structure.render_figure(screen, __desk, __figure, __fig_pos, 0, 0)

    render_structure.render_figure(screen, __desk, __figure_next,
                                   [0, int(constants.NEXT_H / 2 - len(__figure_next[0]) / 2)],
                                   (constants.BLOCKS_H + constants.NEXT_OFFSET) * (constants.BLOCKSIZE + constants.SPACER),
                                   (constants.BLOCKSIZE + constants.SPACER))

    if __gamePaused:
        render_structure.render_pause(screen)

    if __gameOver:
        render_structure.render_game_over(screen, __score)

    if not __gamePaused and not __gameOver:
        tick += 1
        if tick >= constants.maxTicks:
            if 1: #not logic_structure.check_intersect(__desk, __figure, [__fig_pos[0], __fig_pos[1]]):
                if not logic_structure.check_intersect(__desk, __figure, [__fig_pos[0] + 1, __fig_pos[1]]):
                    __fig_pos[0] += 1
                else:
                    __desk = logic_structure.merge(__desk, __figure, __fig_pos)
                    __desk, lines = logic_structure.check_line(copy.deepcopy(__desk))
                    if lines > 0:
                        __lines += lines
                        __destroyed = __destroyed + lines * constants.BLOCKS_H
                        __level = 1 + int(__lines / constants.NEXT_LEVEL_LINES)
                        for i in range(1, lines + 1):
                            __score = __score + len(__desk[0]) * i

                    __figure = __figure_next
                    __figures += 1
                    __fig_pos = [0, int(constants.BLOCKS_H / 2 - len(__figure[0]) / 2)]
                    __figure_next = copy.deepcopy(constants.FIGURES[random.randint(0, constants.FIGURES_COUNT - 1)])
                    __figure_next = logic_structure.set_figure_colour(__figure_next.copy())
                    if logic_structure.check_intersect(__desk, __figure, [__fig_pos[0], __fig_pos[1]]):
                        __gameOver = True
                        pygame.key.set_repeat(0, 0)

            tick = 0

        render_structure.render_info(screen,
                                     [str(constants.BLOCKS_V)+" x " + str(constants.BLOCKS_H),__score,__figures,__level,__lines,__destroyed],
                                     ["Size","Score","Figures","Level","Lines","Bricks"],
                                     (constants.BLOCKS_H + constants.NEXT_OFFSET) * (constants.BLOCKSIZE + constants.SPACER)+constants.SPACER,
                                     ((constants.BLOCKSIZE + constants.SPACER)*(constants.NEXT_V+2) + constants.SPACER))
        pygame.display.set_caption(
                            "TetrisStr - Score:" + str(__score) + " Level:" + str(__level) + " Lines:" + str(
                                __lines) + " Figures:" + str(__figures) + " Bricks:" + str(__destroyed))

    pygame.display.update()

