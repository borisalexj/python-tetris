__author__ = 'user'

import pygame
import constants
from Scenes.Scene import Scene

class GameOverScene(Scene):
    def __init__(self, game):
        # pass
        # self.__game2 = game
        super(GameOverScene, self).__init__(game)

    def render(self):
        super(GameOverScene, self).render()
        game = self.getGame()
        screen = game.get_screen()
        pygame.display.set_caption(
            "Tetris - Score:" + str(game.get_score()) + " Level:" + str(game.get_level()))

        fnt = pygame.font.SysFont(constants.FONTNAME, constants.FONTSIZE + 15)
        GameOverText1 = fnt.render("    Game Over!    ", 1, constants.GO_TEXT_COLOR, constants.GO_BG_COLOR)
        GameOverTxtSize1 = GameOverText1.get_size()
        screen.blit(GameOverText1, (constants.SCREEN_SIZE[0] // 2 - GameOverTxtSize1[0] // 2,
                                    constants.SCREEN_SIZE[1] // 2 - GameOverTxtSize1[1] // 2))

        fnt = pygame.font.SysFont(constants.FONTNAME, constants.FONTSIZE + 7)
        GameOverText2 = fnt.render("  Your score - " + str(game.get_score()) + "  ", 1, constants.GO_TEXT_COLOR, constants.GO_BG_COLOR)
        GameOverTxtSize2 = GameOverText2.get_size()
        screen.blit(GameOverText2, (constants.SCREEN_SIZE[0] // 2 - GameOverTxtSize2[0] // 2,
                                    constants.SCREEN_SIZE[1] // 2 + GameOverTxtSize1[1] // 2))

        fnt = pygame.font.SysFont(constants.FONTNAME, constants.FONTSIZE - 10)
        GameOverText3 = fnt.render("     press any key to continue...     ", 1, constants.GO_TEXT_COLOR, constants.GO_BG_COLOR)
        GameOverTxtSize3 = GameOverText3.get_size()
        screen.blit(GameOverText3, (constants.SCREEN_SIZE[0] // 2 - GameOverTxtSize3[0] // 2,
                                    constants.SCREEN_SIZE[1] // 2 + GameOverTxtSize1[1] // 2 + GameOverTxtSize2[1]))

    def handleEvents(self, events, mods):
        super(GameOverScene, self).handleEvents(events)
        game = self.getGame()

        for event in events:

            if event.type == pygame.KEYDOWN:
                # game.set_scene(constants.PLAYING_SCENE)
                game.set_scene(constants.MENU_SCENE)
                game.reset()



