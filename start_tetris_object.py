""" Start file for Tetris (Object-oriented)"""

import copy
import random

import pygame

from Scenes import GameScene, GameOverScene, PauseScene, MenuScene
from Shared import constants


class Tetris:

    """ Main class for game """

    def __init__(self):
        """ Init for main class, creating initial values """

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Tetris")

        self._clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(constants.SCREEN_SIZE,
                                              pygame.DOUBLEBUF,
                                              32)

        pygame.mouse.set_visible(1)
        self._figures = []
        self.set_figures(constants.CLASSIC_FIGURES)

        self._scenes = (
            GameScene(self),
            GameOverScene(self),
            PauseScene(self),
            MenuScene(self),
            # HighscoreScene(self),
        )

        # self.__currentScene = constants.PLAYING_SCENE
        self._current_scene = constants.MENU_SCENE
        self._sounds = ()
        self.reset()

    def reset(self):
        """ Resets initial values for game """
        self._tick = 0
        self._level = 1
        self._score = 0
        # currentScene = self.__scenes[self.__currentScene]
        # currentScene.__init()
        self._scenes[self._current_scene].__init__(self)

    def set_figures(self, figures):
        """ Creating initial set of figures for game - copying figures
        from constants """
        self._figures = copy.deepcopy(figures)

    def get_rand_figure(self):
        """ Returns random figure from st of figures """
        return copy.deepcopy(
            self._figures[random.randint(0, len(self._figures)) - 1])

    def set_scene(self, scene):
        """ Changes current scene """
        self._current_scene = scene

    def get_screen(self):
        """ Return current scene """
        return self.screen

    def get_level(self):
        """ Changes current scene """
        return self._level

    def set_level(self, level):
        """ Set level """
        self._level = level

    def get_score(self):
        """ Returns score """
        return self._score

    def add_score(self, incr):
        """ Insreases score """
        self._score += incr

    def tick_set_to_zero(self):
        """ For set initial counter for figure on new row """
        self._tick = 0

    def tick_set_to_max(self):
        """ For move figure on next row down """
        self._tick = constants.maxTicks

    def tick_increase(self):
        """ For increase ticks before move figure on next row down """
        self._tick += 1

    def get_tick(self):
        """ Returns current tick for figure on the row """
        return self._tick

    def start(self):
        """ Main method for game with loop """
        while 1:
            self._clock.tick(
                constants.pyTimer
                + (self._level - 1) * constants.levelMultiplier)
            self.screen.fill((0, 0, 0))
            current_scene = self._scenes[self._current_scene]
            current_scene.handleEvents(pygame.event.get(),
                                       pygame.key.get_mods())
            current_scene.render()
            pygame.display.update()

Tetris().start()
