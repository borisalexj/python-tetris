""" Start file for Tetris (Procedural)"""

import random
import copy

import pygame

from Shared import constants, logic_procedural, render_procedural

# from Scenes import GameScene
# from Scenes import *

_lives = 1
_score = 0
_level = 1  # Level
_destroyed = 0
_lines = 0
_figures = 0
_desk = logic_procedural.create_desk(constants.BLOCKS_V, constants.BLOCKS_H)
_desk_next = logic_procedural.create_desk(constants.NEXT_V, constants.NEXT_H)
_gamePaused = False
_gameOver = False
_figure = copy.deepcopy(constants.FIGURES[random.randint(0, constants.FIGURES_COUNT-1)])
_figure = logic_procedural.set_figure_colour(_figure.copy())
_figures += 1
_fig_pos = [0, int(constants.BLOCKS_H / 2 - len(_figure[0]) / 2)]
_figure_next = copy.deepcopy(constants.FIGURES[random.randint(0, constants.FIGURES_COUNT-1)])  # random.randint(0,constants.FIGURES_COUNT-1)])
_figure_next = logic_procedural.set_figure_colour(_figure_next.copy())

pygame.init()
pygame.mixer.init()
pygame.display.set_caption(
    "TetrisProc - Score:" + str(_score) + " Level:" + str(_level) + " Lines:" + str(_lines) + " Figures:" + str(
        _figures) + " Bricks:" + str(_destroyed))

_clock = pygame.time.Clock()
tick = 1

screen = pygame.display.set_mode(constants.SCREEN_SIZE, pygame.DOUBLEBUF, 32)

pygame.mouse.set_visible(1)
pygame.key.set_repeat(constants.KEYBOARD_REPEAT[0], constants.KEYBOARD_REPEAT[1])

# scene = Scene(self)

while 1:
    screen.fill(constants.BG_COLOR)

    _clock.tick(constants.pyTimer + (_level - 1) * constants.levelMultiplier)
    events = pygame.event.get()
    mods = pygame.key.get_mods()

    for event in events:
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN and _gamePaused:
            _gamePaused = False
            pygame.key.set_repeat(constants.KEYBOARD_REPEAT[0],
                                  constants.KEYBOARD_REPEAT[1])

        if event.type == pygame.KEYDOWN and _gameOver:
            _lives = 1
            _score = 0
            _level = 1  # Level
            _destroyed = 0
            _lines = 0
            _figures = 0
            _desk = logic_procedural.create_desk(
                constants.BLOCKS_V, constants.BLOCKS_H)
            _gameOver = False
            _figure = copy.deepcopy(
                constants.FIGURES[random.randint(0, constants.FIGURES_COUNT - 1)])
            _figure = logic_procedural.set_figure_colour(_figure.copy())
            _figures += 1
            _fig_pos = [0, int(constants.BLOCKS_H / 2 - len(_figure[0]) / 2)]
            _figure_next = copy.deepcopy(constants.FIGURES[6])  # random.randint(0,constants.FIGURES_COUNT-1)])
            _figure_next = logic_procedural.set_figure_colour(_figure_next.copy())
            pygame.key.set_repeat(250, 25)

        if event.type == pygame.KEYDOWN  and not _gameOver:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                exit()

            if event.key == pygame.K_p:
                _gamePaused = True
                pygame.key.set_repeat(0, 0)

            if event.key == pygame.K_RIGHT and mods ==64:
                constants.BLOCKS_H +=1
                for y in range(len(_desk)): _desk[y].append(0)

            if event.key == pygame.K_LEFT and mods ==64 and constants.BLOCKS_H>5:
                constants.BLOCKS_H -=1
                for y in range(len(_desk)): _desk[y].pop()
                if _fig_pos[1]+len(_figure[0])>len(_desk[0]):
                    _fig_pos[1] -=1

            if event.key == pygame.K_DOWN and mods ==64:
                constants.BLOCKS_V +=1
                _desk = logic_procedural.add_empty_line(copy.deepcopy(_desk))

            if event.key == pygame.K_UP and mods ==64 and constants.BLOCKS_V>5:
                constants.BLOCKS_V -=1
                _desk.pop()

            if (event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and mods ==64:
                constants.SCREEN_SIZE = constants.calculate_screen_size(
                    constants.BLOCKS_H, constants.BLOCKS_V)
                screen = pygame.display.set_mode(constants.SCREEN_SIZE, pygame.DOUBLEBUF, 32)

            if (event.key == pygame.K_RIGHT or event.key == pygame.K_KP6) and mods == 0:
                if not logic_procedural.check_intersect(_desk, _figure, [_fig_pos[0], _fig_pos[1] + 1]):
                    _fig_pos[1] += 1

            if (event.key == pygame.K_LEFT or event.key == pygame.K_KP4)  and mods == 0:
                if not logic_procedural.check_intersect(_desk, _figure, [_fig_pos[0], _fig_pos[1] - 1]):
                    _fig_pos[1] -= 1

            if (event.key == pygame.K_5 or event.key == pygame.K_UP or event.key == pygame.K_KP5) and mods == 0:
                tmp_rotated, tmp_pos = logic_procedural.rotate(_figure, _fig_pos)
                if len(tmp_rotated[0]) + tmp_pos[1] >= len(_desk[0]): #len(__figure[0]) + __fig_pos[1] == len(__desk[0]): # trying to move on -1 from right
                    tmp_pos[1] -= (len(tmp_rotated[0]) + tmp_pos[1]) - len(_desk[0])
                    # print("Fuck")
                if tmp_pos[1] <0: #__fig_pos[1] == 0:  # tryin to move on +1 from left
                    tmp_pos[1] = 0

                if not logic_procedural.check_intersect(_desk, tmp_rotated, tmp_pos):  # simple turn on an empty space
                    _figure, _fig_pos = tmp_rotated, tmp_pos # logic_structure.rotate(__figure, __fig_pos)

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
                if not logic_procedural.check_intersect(_desk, _figure, [_fig_pos[0] + 1, _fig_pos[1]]):
                    _fig_pos[0] += 1
                else:
                    tick = constants.maxTicks - 1

            if (event.key == pygame.K_KP8) and mods == 0:
                if not logic_procedural.check_intersect(_desk, _figure, [_fig_pos[0] - 1, _fig_pos[1]]):
                    _fig_pos[0] -= 1
                    if _fig_pos[0] <0 : _fig_pos[0]=0

    render_procedural.render_desk(screen, _desk, 0, 0)
    render_procedural.render_desk(screen, _desk_next,
                                 (constants.BLOCKS_H + constants.NEXT_OFFSET) * (
                                 constants.BLOCKSIZE + constants.SPACER),
                                 (constants.BLOCKSIZE + constants.SPACER))

    render_procedural.render_figure(screen, _desk, _figure, _fig_pos, 0, 0)

    render_procedural.render_figure(screen, _desk, _figure_next,
                                   [0, int(constants.NEXT_H / 2 - len(_figure_next[0]) / 2)],
                                   (constants.BLOCKS_H + constants.NEXT_OFFSET) * (
                                   constants.BLOCKSIZE + constants.SPACER),
                                   (constants.BLOCKSIZE + constants.SPACER))

    if _gamePaused:
        render_procedural.render_pause(screen)

    if _gameOver:
        render_procedural.render_game_over(screen, _score)

    if not _gamePaused and not _gameOver:
        tick += 1
        if tick >= constants.maxTicks:
            if 1: #not logic_structure.check_intersect(__desk, __figure, [__fig_pos[0], __fig_pos[1]]):
                if not logic_procedural.check_intersect(_desk, _figure, [_fig_pos[0] + 1, _fig_pos[1]]):
                    _fig_pos[0] += 1
                else:
                    _desk = logic_procedural.merge(_desk, _figure, _fig_pos)
                    _desk, lines = logic_procedural.check_line(copy.deepcopy(_desk))
                    if lines > 0:
                        _lines += lines
                        _destroyed = _destroyed + lines * constants.BLOCKS_H
                        _level = 1 + int(_lines / constants.NEXT_LEVEL_LINES)
                        for i in range(1, lines + 1):
                            _score = _score + len(_desk[0]) * i

                    _figure = _figure_next
                    _figures += 1
                    _fig_pos = [0, int(constants.BLOCKS_H / 2 - len(_figure[0]) / 2)]
                    _figure_next = copy.deepcopy(
                        constants.FIGURES[random.randint(0, constants.FIGURES_COUNT - 1)])
                    _figure_next = logic_procedural.set_figure_colour(_figure_next.copy())
                    if logic_procedural.check_intersect(_desk, _figure, [_fig_pos[0], _fig_pos[1]]):
                        _gameOver = True
                        pygame.key.set_repeat(0, 0)

            tick = 0

        render_procedural.render_info(screen,
                                     [str(constants.BLOCKS_V)+" x " + str(
                                         constants.BLOCKS_H),_score,_figures,_level,_lines,_destroyed],
                                     ["Size","Score","Figures","Level","Lines","Bricks"],
                                     (constants.BLOCKS_H + constants.NEXT_OFFSET) * (
                                     constants.BLOCKSIZE + constants.SPACER)+ constants.SPACER,
                                     ((constants.BLOCKSIZE + constants.SPACER)*(
                                     constants.NEXT_V+2) + constants.SPACER))
        pygame.display.set_caption(
                            "TetrisProc - Score:" + str(_score) + " Level:" + str(_level) + " Lines:" + str(
                                _lines) + " Figures:" + str(_figures) + " Bricks:" + str(_destroyed))

    pygame.display.update()

