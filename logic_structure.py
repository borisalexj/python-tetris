__author__ = 'user'
import constants
import random
# import copy

def create_desk(vert_count, horiz_count):
    desk = []
    for y in range(vert_count):
        row = []
        for x in range(horiz_count):
            row.append(0)
        desk.append(row)

    return desk

def set_figure_colour(figure):
    colour = random.randint(1, constants.COLORS_COUNT - 1)
    for y in range(len(figure)):
        for x in range(len(figure[y])):
            figure[y][x] = figure[y][x] * colour
    return figure

def check_intersect(desk, figure, fig_pos):
    intersect = False
    # check boundary
    if fig_pos[1] + len(figure[0]) > constants.BLOCKS_H or fig_pos[1] < 0:  # left and right
        intersect = True
        return intersect
    if fig_pos[0] + len(figure) > constants.BLOCKS_V:  # bottom
        intersect = True
        return intersect

    # check intersect with figures
    for y in range(len(figure)):
        for x in range(len(figure[y])):
            if figure[y][x] > 0 and desk[fig_pos[0] + y][fig_pos[1] + x] > 0:
                intersect = True
                return intersect

    return intersect

def merge(desk, figure, fig_pos):
    for y in range(len(figure)):
        for x in range(len(figure[y])):
            if figure[y][x] != 0:
                desk[fig_pos[0] + y][fig_pos[1] + x] = figure[y][x]
    return desk

def rotate(figure, fig_pos):
    new_fig = []
    new_pos = []
    for x in range(len(figure[0])):
        row = []
        for y in reversed(range(len(figure))):
            row.append(figure[y][x])
        new_fig.append(row)
    if len(figure) > 3:
        new_pos = [fig_pos[0], fig_pos[1] - round(len(figure[0]) / 2 )-1]#- len(new_fig[0]) / 2)]

    elif len(figure[0]) > 3:
        # print("++++")
        new_pos = [fig_pos[0], fig_pos[1] + 1]
    else:
        new_pos = fig_pos

    return new_fig, new_pos

def check_line(desk):
    lines = 0
    for y in range(len(desk)):
        full = True
        for x in range(len(desk[y])):
            if desk[y][x] == 0:
                full = False
        if full:
            desk.pop(y)
            desk = add_empty_line(desk)
            lines += 1

    return desk, lines

def add_empty_line(desk):
    row = []
    for c in range(constants.BLOCKS_H):
        row.append(0)
    desk = [row, ] + desk[:]
    return  desk

