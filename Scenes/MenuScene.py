__author__ = 'user'

import pygame
import constants
from Scenes.Scene import Scene

class MenuScene(Scene):
    def __init__(self, game):
        # pass
        # self.__game2 = game
        super().__init__(game)

    def render(self):
        super().render()
        game = self.getGame()
        screen = game.get_screen()

        fnt = pygame.font.SysFont(constants.FONTNAME, constants.FONTSIZE + 7)
        texts = ["1 - Classic tetris","2 - Pentamino","q/esc - Quit"]

        for i in range(len(texts)):
            MenuText = fnt.render(texts[i], 1, (255, 0, 0), (0, 0, 0))
            MenuTxtSize = MenuText.get_size()
            screen.blit(MenuText, (constants.SCREEN_SIZE[0] // 2 - MenuTxtSize[0] // 2,
                                        constants.SCREEN_SIZE[1] // 2 - MenuTxtSize[1] // 2 + MenuTxtSize[1] * i))


    def handleEvents(self, events, mods):
        super().handleEvents(events)
        game = self.getGame()

        for event in events:
            if event.type == pygame.KEYDOWN:
                # print(event.key)

                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    # print("classic")
                    game.set_figures(constants.CLASSIC_FIGURES)
                    constants.NEXT_H = constants.CLASSIC_FIGURE_SIZE
                    constants.NEXT_V = constants.CLASSIC_FIGURE_SIZE

                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    # print("pentamino")
                    game.set_figures(constants.PENTAMINO_FIGURES)
                    constants.NEXT_H = constants.PENTAMINO_FIGURE_SIZE
                    constants.NEXT_V = constants.PENTAMINO_FIGURE_SIZE

                # constants.FIGURES_COUNT = len(constants.FIGURES)
                game.set_scene(constants.PLAYING_SCENE)
                game.reset()





