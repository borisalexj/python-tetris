__author__ = 'user'

import copy

from Shared import constants


class Desk:
    def __init__(self,vert_count,horiz_count):

        self.__desk = []
        for y in range(vert_count):
            row = []
            for x in range(horiz_count):
                row.append(0)
            self.__desk.append(row)

    def get_desk(self):
        return copy.deepcopy(self.__desk)

    def check_intersect(self, figure, fig_pos):
        desk = self.get_desk()
        intersect = False
        # check boundary
        if fig_pos[1] + len(figure[0]) > constants.BLOCKS_H or fig_pos[1] < 0:  # left and right
            intersect = True
            return intersect
        if fig_pos[0] + len(figure) > constants.BLOCKS_V:  # bottom
            intersect = True
            return intersect
        if fig_pos[0] < 0: # up
            intersect = True
            return intersect

        # check intersect with figures
        for y in range(len(figure)):
            for x in range(len(figure[y])):
                if figure[y][x] > 0 and desk[fig_pos[0] + y][fig_pos[1] + x] > 0:
                    intersect = True
                    return intersect

        return intersect

    def merge(self, figure, fig_pos):
        for y in range(len(figure)):
            for x in range(len(figure[y])):
                if figure[y][x] != 0:
                    self.__desk[fig_pos[0] + y][fig_pos[1] + x] = figure[y][x]
        # return desk


    def check_line(self):
        lines = 0
        for y in range(len(self.__desk)):
            full = True
            for x in range(len(self.__desk[y])):
                if self.__desk[y][x] == 0:
                    full = False
            if full:
                self.__desk.pop(y)
                self.add_empty_line()
                lines += 1

        return lines


    def add_empty_line(self):
        row = []
        for c in range(constants.BLOCKS_H):
            row.append(0)
        self.__desk = [row, ] + self.__desk[:]
        # return  desk

