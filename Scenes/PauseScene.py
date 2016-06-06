__author__ = 'user'

import pygame
import constants
from Scenes.Scene import Scene

class PauseScene(Scene):
    def __init__(self, game):
        super().__init__(game)

    def render(self):
        super().render()
        game = self.getGame()
        screen = game.get_screen()
        pygame.display.set_caption(
            "Tetris - Score:" + str(game.get_score()) + " Level:" + str(game.get_level()))

        fnt = pygame.font.SysFont(constants.FONTNAME, constants.FONTSIZE + 15)
        PauseText1 = fnt.render("    Paused!    ", 1, constants.P_TEXT_COLOR, constants.P_BG_COLOR)
        PauseTxtSize1 = PauseText1.get_size()
        screen.blit(PauseText1, (constants.SCREEN_SIZE[0] // 2 - PauseTxtSize1[0] // 2,
                                    constants.SCREEN_SIZE[1] // 2 - PauseTxtSize1[1] // 2))

        fnt = pygame.font.SysFont(constants.FONTNAME, constants.FONTSIZE + 7)
        PauseText2 = fnt.render("  Your score - " + str(game.get_score()) + "  ", 1, constants.P_TEXT_COLOR, constants.P_BG_COLOR)
        PauseTxtSize2 = PauseText2.get_size()
        screen.blit(PauseText2, (constants.SCREEN_SIZE[0] // 2 - PauseTxtSize2[0] // 2,
                                    constants.SCREEN_SIZE[1] // 2 + PauseTxtSize1[1] // 2))

        fnt = pygame.font.SysFont(constants.FONTNAME, constants.FONTSIZE - 10)
        PauseText3 = fnt.render("     press any key to continue...     ", 1, constants.P_TEXT_COLOR, constants.P_BG_COLOR)
        PauseTxtSize3 = PauseText3.get_size()
        screen.blit(PauseText3, (constants.SCREEN_SIZE[0] // 2 - PauseTxtSize3[0] // 2,
                                    constants.SCREEN_SIZE[1] // 2 + PauseTxtSize1[1] // 2 + PauseTxtSize2[1]))

    def handleEvents(self, events, mods):
        super().handleEvents(events)
        game = self.getGame()

        for event in events:

            if event.type == pygame.KEYDOWN:
                game.set_scene(constants.PLAYING_SCENE)
                pygame.key.set_repeat(constants.KEYBOARD_REPEAT[0],constants.KEYBOARD_REPEAT[1])




