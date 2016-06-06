__author__ = 'user'
import constants
import pygame
# import logic_structure

def render_desk(screen, desk, start_x, start_y):
    for y in range(len(desk)):
        for x in range(len(desk[y])):
            pygame.draw.rect(screen, constants.COLORS[desk[y][x]],
                             (start_x + (constants.BLOCKSIZE + constants.SPACER) * x + constants.SPACER,
                              start_y + (constants.BLOCKSIZE + constants.SPACER) * y + constants.SPACER,
                              constants.BLOCKSIZE,
                              constants.BLOCKSIZE), 0)

def render_figure(screen, desk, figure, fig_pos, start_x, start_y):
    for y in range(len(figure)):
        for x in range(len(figure[y])):
            if figure[y][x] != 0:
                pygame.draw.rect(screen, constants.COLORS[figure[y][x]],
                                 (start_x + (constants.BLOCKSIZE + constants.SPACER) * (x + fig_pos[1]) + constants.SPACER,
                                  start_y + (constants.BLOCKSIZE + constants.SPACER) * (y + fig_pos[0]) + constants.SPACER,
                                  constants.BLOCKSIZE,
                                  constants.BLOCKSIZE),0)

def render_pause(screen):
    fnt = pygame.font.SysFont(constants.FONTNAME, constants.FONTSIZE)
    PauseText1 = fnt.render("    Game Paused!    ", 1, constants.P_TEXT_COLOR, constants.P_BG_COLOR)
    PauseTxtSize1 = PauseText1.get_size()
    screen.blit(PauseText1, (
    constants.SCREEN_SIZE[0] // 2 - PauseTxtSize1[0] // 2, constants.SCREEN_SIZE[1] // 2 - PauseTxtSize1[1] // 2))

    fnt = pygame.font.SysFont(constants.FONTNAME, constants.FONTSIZE - 10)
    PauseText2 = fnt.render(" Press any key to continue ", 1, constants.P_TEXT_COLOR, constants.P_BG_COLOR)
    PauseTxtSize2 = PauseText2.get_size()
    screen.blit(PauseText2, (
    constants.SCREEN_SIZE[0] // 2 - PauseTxtSize2[0] // 2, constants.SCREEN_SIZE[1] // 2 + PauseTxtSize1[1] // 2))

def render_game_over(screen, score):
    fnt = pygame.font.SysFont(constants.FONTNAME, constants.FONTSIZE + 15)
    GameOverText1 = fnt.render("    Game Over!    ", 1, constants.GO_TEXT_COLOR, constants.GO_BG_COLOR)
    GameOverTxtSize1 = GameOverText1.get_size()
    screen.blit(GameOverText1, (constants.SCREEN_SIZE[0] // 2 - GameOverTxtSize1[0] // 2,
                                constants.SCREEN_SIZE[1] // 2 - GameOverTxtSize1[1] // 2))

    fnt = pygame.font.SysFont(constants.FONTNAME, constants.FONTSIZE + 7)
    GameOverText2 = fnt.render("  Your score - " + str(score) + "  ", 1, constants.GO_TEXT_COLOR, constants.GO_BG_COLOR)
    GameOverTxtSize2 = GameOverText2.get_size()
    screen.blit(GameOverText2, (constants.SCREEN_SIZE[0] // 2 - GameOverTxtSize2[0] // 2,
                                constants.SCREEN_SIZE[1] // 2 + GameOverTxtSize1[1] // 2))

    fnt = pygame.font.SysFont(constants.FONTNAME, constants.FONTSIZE - 10)
    GameOverText3 = fnt.render("     press any key to continue...     ", 1, constants.GO_TEXT_COLOR, constants.GO_BG_COLOR)
    GameOverTxtSize3 = GameOverText3.get_size()
    screen.blit(GameOverText3, (constants.SCREEN_SIZE[0] // 2 - GameOverTxtSize3[0] // 2,
                                constants.SCREEN_SIZE[1] // 2 + GameOverTxtSize1[1] // 2 + GameOverTxtSize2[1]))

def render_info(screen, values, names, start_x, start_y):
    for cnt in range(len(values)):
        fnt = pygame.font.SysFont(constants.FONTNAME, constants.FONTSIZE - 15)
        fnt.set_bold(True)
        txt = fnt.render(names[cnt]+ ": " + str(values[cnt]) , 1, constants.TEXT_COLOR, constants.BG_COLOR)
        txtSize = txt.get_size()
        screen.blit(txt, (start_x, start_y + txtSize[1]*cnt))

