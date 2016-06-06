__author__ = 'user'

import pygame
import desk_class, constants
# from Scenes import GameScene
import copy
import random
from Scenes import *


class Tetris:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Tetris")

        self.__clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(constants.SCREEN_SIZE, pygame.DOUBLEBUF, 32)

        pygame.mouse.set_visible(1)
        self.__figures = []
        self.set_figures(constants.CLASSIC_FIGURES)

        self.__scenes = (
            GameScene(self),
            GameOverScene(self),
            PauseScene(self),
            MenuScene(self),
            # HighscoreScene(self),
        )

        # self.__currentScene = constants.PLAYING_SCENE
        self.__currentScene = constants.MENU_SCENE
        self.__sounds = ()
        self.reset()

    def reset(self):
        self.__tick = 0
        self.__level = 1
        self.__score = 0
        # currentScene = self.__scenes[self.__currentScene]
        # currentScene.__init()
        self.__scenes[self.__currentScene].__init__(self)

    def set_figures(self, figures):
        self.__figures = copy.deepcopy(figures)

    def get_rand_figure(self):
        # i = random.randint(0, len(self.__figures))
        # print(i)
        # print()
        return copy.deepcopy(self.__figures[random.randint(0, len(self.__figures)) - 1])

    def set_scene(self, scene):
        self.__currentScene = scene

    def get_screen(self):
        return self.screen

    def get_level(self):
        return self.__level

    def set_level(self, level):
        self.__level = level

    def get_score(self):
        return self.__score

    def add_score(self, incr):
        self.__score += incr

    def tick_set_to_zero(self):
        self.__tick = 0

    def tick_set_to_max(self):
        self.__tick = constants.maxTicks

    def tick_increase(self):
        self.__tick += 1

    def get_tick(self):
        return self.__tick

    def start(self):
        while 1:
            self.__clock.tick(constants.pyTimer + (self.__level - 1) * constants.levelMultiplier)
            self.screen.fill((0, 0, 0))
            currentScene = self.__scenes[self.__currentScene]
            currentScene.handleEvents(pygame.event.get(), pygame.key.get_mods())
            currentScene.render()
            pygame.display.update()


Tetris().start()
