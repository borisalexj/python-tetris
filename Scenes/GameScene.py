__author__ = 'user'

import pygame

from Shared import constants
from Scenes.Scene import Scene
from Shared.desk import Desk
from Shared.figure import Figure


class GameScene(Scene):
    def __init__(self, game):
        super(GameScene, self).__init__(game)
        pygame.key.set_repeat(constants.KEYBOARD_REPEAT[0],
                              constants.KEYBOARD_REPEAT[1])
        self.__destroyed = 0
        self.__lines = 0
        self.__figures = 0
        self.__desk = Desk(constants.BLOCKS_V, constants.BLOCKS_H)
        self.__desk_next = Desk(constants.NEXT_V, constants.NEXT_H)
        self.__figure = Figure(game.get_rand_figure())
        self.__figures += 1
        self.__figure.set_position(0, int(constants.BLOCKS_H / 2 - self.__figure.get_with() / 2))
        self.__figure_next = Figure(game.get_rand_figure())
        self.__figure_next.set_position(0, int(constants.NEXT_H / 2 - self.__figure_next.get_with() / 2))


    def render(self):
        super(GameScene, self).render()
        game = self.getGame()
        screen = game.get_screen()
        pygame.display.set_caption(
            "TetrisObj - Score:" + str(game.get_score()) + " Level:" + str(game.get_level()) + " Lines:" + str(self.__lines) +
            " Figures:" + str(self.__figures) + " Bricks:" + str(self.__destroyed))
        self.render_desk(screen,self.__desk.get_desk(),0,0)
        self.render_desk(screen,self.__desk_next.get_desk(),
                         (constants.BLOCKS_H + constants.NEXT_OFFSET) * (
                         constants.BLOCKSIZE + constants.SPACER),
                         (constants.BLOCKSIZE + constants.SPACER))

        self.render_figure(screen,self.__desk.get_desk(),self.__figure.get_figure(),self.__figure.get_position(),0,0)

        self.render_figure(screen,self.__desk.get_desk(),self.__figure_next.get_figure(),self.__figure_next.get_position(),
                           (constants.BLOCKS_H + constants.NEXT_OFFSET) * (
                           constants.BLOCKSIZE + constants.SPACER),
                           (constants.BLOCKSIZE + constants.SPACER))
        self.render_info(screen,
                         [str(constants.BLOCKS_V)+" x " + str(constants.BLOCKS_H),game.get_score(),self.__figures,game.get_level(),self.__lines,self.__destroyed],
                         ["Size","Score","Figures","Level","Lines","Bricks"],
                         (constants.BLOCKS_H + constants.NEXT_OFFSET) * (
                         constants.BLOCKSIZE + constants.SPACER)+ constants.SPACER,
                         ((constants.BLOCKSIZE + constants.SPACER)*(
                         constants.NEXT_V+2) + constants.SPACER))

    def render_desk(self,screen, desk, start_x, start_y):
        for y in range(len(desk)):
            for x in range(len(desk[y])):
                pygame.draw.rect(screen, constants.COLORS[desk[y][x]],
                                 (start_x + (
                                 constants.BLOCKSIZE + constants.SPACER) * x + constants.SPACER,
                                  start_y + (
                                  constants.BLOCKSIZE + constants.SPACER) * y + constants.SPACER,
                                  constants.BLOCKSIZE,
                                  constants.BLOCKSIZE), 0)

    def render_figure(self,screen, desk, figure, fig_pos, start_x, start_y):
        for y in range(len(figure)):
            for x in range(len(figure[y])):
                if figure[y][x] != 0:
                    pygame.draw.rect(screen, constants.COLORS[figure[y][x]],
                                     (start_x + (
                                     constants.BLOCKSIZE + constants.SPACER) * (x + fig_pos[1]) + constants.SPACER,
                                      start_y + (
                                      constants.BLOCKSIZE + constants.SPACER) * (y + fig_pos[0]) + constants.SPACER,
                                      constants.BLOCKSIZE,
                                      constants.BLOCKSIZE),0)

    def render_info(self,screen, values, names, start_x, start_y):
        fnt = pygame.font.SysFont(constants.FONTNAME, constants.FONTSIZE - 15)
        fnt.set_bold(True)
        for cnt in range(len(values)):
            txt = fnt.render(names[cnt]+ ": " + str(values[cnt]) , 1, constants.TEXT_COLOR, constants.BG_COLOR)
            txtSize = txt.get_size()
            screen.blit(txt, (start_x, start_y + txtSize[1]*cnt))

    def handleEvents(self, events, mods):
        game = self.getGame()

        super(GameScene, self).handleEvents(events)

        for event in events:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pygame.key.set_repeat(0, 0)
                    game.set_scene(constants.PAUSE_SCENE)

                if (event.key == pygame.K_RIGHT or event.key == pygame.K_KP6) and mods == 0:
                    if not self.__desk.check_intersect(self.__figure.get_figure(), [self.__figure.get_position()[0], self.__figure.get_position()[1] + 1]):
                        self.__figure.change_position(0, 1)

                if (event.key == pygame.K_LEFT or event.key == pygame.K_KP4) and mods == 0:
                    if not self.__desk.check_intersect(self.__figure.get_figure(), [self.__figure.get_position()[0], self.__figure.get_position()[1] - 1]):
                        self.__figure.change_position(0, -1)

                if (event.key == pygame.K_5 or event.key == pygame.K_UP or event.key == pygame.K_KP5) and mods == 0:
                    tmp_rotated, tmp_pos = self.__figure.get_rotated()
                    if len(tmp_rotated[0]) + tmp_pos[1] >= len(self.__desk.get_desk()[0]): # trying to move on -1 from right
                        tmp_pos[1] -= (len(tmp_rotated[0]) + tmp_pos[1]) - len(self.__desk.get_desk()[0])
                    if tmp_pos[1] < 0: # tryin to move on +1 from left
                        tmp_pos[1] = 0

                    if not self.__desk.check_intersect(tmp_rotated, tmp_pos):  # simple turn on an empty space
                        self.__figure.set_figure(tmp_rotated)
                        self.__figure.set_position(tmp_pos[0],tmp_pos[1])

                if (event.key == pygame.K_SPACE or event.key == pygame.K_DOWN or event.key == pygame.K_KP2) and mods == 0:
                    if not self.__desk.check_intersect(self.__figure.get_figure(), [self.__figure.get_position()[0]+1, self.__figure.get_position()[1]]):
                        self.__figure.change_position(1, 0)
                    else:
                        game.tick_set_to_max()

                if (event.key == pygame.K_KP8) and mods == 0:
                    if not self.__desk.check_intersect(self.__figure.get_figure(), [self.__figure.get_position()[0]-1, self.__figure.get_position()[1]]):
                        self.__figure.change_position(-1, 0)

        game.tick_increase()
        if game.get_tick() >= constants.maxTicks :
            if not self.__desk.check_intersect(self.__figure.get_figure(), [self.__figure.get_position()[0]+1, self.__figure.get_position()[1]]):
                self.__figure.set_position(self.__figure.get_position()[0]+1, self.__figure.get_position()[1])
            else:
                self.__desk.merge(self.__figure.get_figure(), self.__figure.get_position())
                lines = self.__desk.check_line()
                if lines >0:
                    self.__lines += lines
                    self.__destroyed += lines* constants.BLOCKS_H
                    game.set_level(1 + int(self.__lines / constants.NEXT_LEVEL_LINES))
                for i in range(1, lines + 1):
                    game.add_score(constants.BLOCKS_H * i)

                self.__figure = self.__figure_next
                self.__figures += 1
                self.__figure.set_position(0, int(constants.BLOCKS_H / 2 - self.__figure.get_with() / 2))
                self.__figure_next = Figure(game.get_rand_figure())
                self.__figure_next.set_position(0, int(constants.NEXT_H / 2 - self.__figure_next.get_with() / 2))
                if self.__desk.check_intersect(self.__figure.get_figure(),self.__figure.get_position()):
                    pygame.key.set_repeat(0, 0)
                    game.set_scene(constants.GAMEOVER_SCENE)

            game.tick_set_to_zero()







