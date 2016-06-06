__author__ = 'user'

import pygame

class Scene:
    def __init__(self, game):
        self.__game = game

    def render(self):
        pass

    def getGame(self):
        return self.__game

    def handleEvents(self, events):
        pass

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    exit()

