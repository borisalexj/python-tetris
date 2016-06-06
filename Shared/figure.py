__author__ = 'user'
import copy
import random

from Shared import constants


class Figure:
    __figures_count = 0
    def __init__(self, figure):
        # self.__figure = copy.deepcopy(constants.FIGURES[random.randint(0, constants.FIGURES_COUNT - 1)])
        self.__figure = figure
        # print("+++++++++++")
        Figure.__figures_count += 1
        # self.__color = random.randint(1, constants.COLORS_COUNT - 1)
        self.__figure = self.set_color(self.__figure)
        self.__position = [0,0] #y,x
        for i in range(random.randint(0,3)):
            self.rotate()
            # self.__figure, self.__position = self.get_rotated()

    @property
    def count(self):
        return Figure.__figures_count

    def set_color(self, figure):
        colour = random.randint(1, constants.COLORS_COUNT - 1)
        for y in range(len(figure)):
            for x in range(len(figure[y])):
                figure[y][x] = figure[y][x] * colour
        return figure

    def rotate(self):
        self.__figure, self.__position = self.get_rotated()

    def get_rotated(self):
        new_fig = []
        new_pos = []
        for x in range(len(self.__figure[0])):
            row = []
            for y in reversed(range(len(self.__figure))):
                row.append(self.__figure[y][x])
            new_fig.append(row)
        if len(self.__figure) > 3 and len(self.__figure[0])==1:
            new_pos = [self.__position[0], self.__position[1] - round(len(self.__figure[0]) / 2) - 1 ]# - len(new_fig[0]) / 2)]
            # new_pos = [self.__position[0], round(self.__position[1] + len(self.__figure[0]) / 2 - len(new_fig[0]) / 2)]
        elif len(self.__figure) > 3 and len(self.__figure[0])>1:
            new_pos = [self.__position[0], self.__position[1] - round(len(self.__figure[0]) / 2)  ]# - len(new_fig[0]) / 2)]

        elif len(self.__figure[0]) > 3:
            new_pos = [self.__position[0], self.__position[1] + 1]
        else:
            new_pos = self.__position

        return new_fig, new_pos

    def get_figure(self):
        return copy.deepcopy(self.__figure)

    def set_figure(self, newFigure):
        self.__figure = newFigure

    def get_color(self):
        return self.__color

    def set_position(self,y,x):
        self.__position = [y,x]
        # if self.__position[0] < 0:
        #     self.__position[0] = 0

    def change_position(self,incY, incX):
        self.__position[0] += incY
        self.__position[1] += incX


    def get_position(self):
        return self.__position

    def get_size(self):
        return len(self.__figure),len(self.__figure[0])

    def get_with(self):
        return len(self.__figure[0])

    def get_height(self):
        return len(self.__figure)
