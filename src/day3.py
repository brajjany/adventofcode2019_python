from helpers import get_data_comma
import pandas as pd
import numpy as np


def get_direction_arrays(data=[]):
    # returns all direction arrays and its distance
    rights = []
    lefts = []
    ups = []
    downs = []
    directions = []
    all_values = []

    for element in data:
        if element[0] == 'R':
            rights.append(int(element[1:]))
        if element[0] == 'L':
            lefts.append(int(element[1:]))
        if element[0] == 'D':
            downs.append(int(element[1:]))
        if element[0] == 'U':
            ups.append(int(element[1:]))
        directions.append(str(element[0]))
        all_values.append(element[1:])
    return rights, lefts, ups, downs, all_values, directions


def get_coordinates(init, data):
    # return dict of lines with coordinates, i.e. {line1 : [(x_1,y_1), (x_2,y_2)], line2 : [(x_2,y_2),(x_3,y_3]}
    lines = {}
    first_coordinates = init
    second_coordinates = init

    for i, element in enumerate(data):
        if element[0] == 'R':
            x = first_coordinates[0] + int(element[1:])
            y = first_coordinates[1]
            second_coordinates = (x, y)

        elif element[0] == 'L':
            x = first_coordinates[0] - int(element[1:])
            y = first_coordinates[1]
            second_coordinates = (x, y)

        elif element[0] == 'D':
            x = first_coordinates[0]
            y = first_coordinates[1] - int(element[1:])
            second_coordinates = (x, y)

        elif element[0] == 'U':
            x = first_coordinates[0]
            y = first_coordinates[1] + int(element[1:])
            second_coordinates = (x, y)
        else:
            Exception("Something went wrong.")

        if "Line" + str(i) not in lines.keys():
            lines["Line" + str(i)] = (first_coordinates, second_coordinates)
        else:
            Exception("Something went wrong.")

        first_coordinates = second_coordinates

    return lines


def day_three_a():
    data = get_data_comma(data='day3_data')

    init = (0, 0)

    # Create array of coordinates
    coordinates_a = get_coordinates(init=init, data=data[0])
    coordinates_b = get_coordinates(init=init, data=data[1])

    return coordinates_a, coordinates_b


'''
print('R sum {} len {}: {}'.format(sum(day_three_a()[0]), len(day_three_a()[0]), day_three_a()[0]))
print('L sum {} len {}: {}'.format(sum(day_three_a()[1]), len(day_three_a()[1]), day_three_a()[1]))
print('U sum {} len {}: {}'.format(sum(day_three_a()[2]), len(day_three_a()[2]), day_three_a()[2]))
print('D sum {} len {}: {}'.format(sum(day_three_a()[3]), len(day_three_a()[3]), day_three_a()[3]))
print('Values {} | {}'.format(len(day_three_a()[4]),day_three_a()[4]))
print('Directions {} | {}'.format(len(day_three_a()[5]),day_three_a()[5]))

print('ALL {}'.format(len(get_data_comma(data='day3_data')[0])))'''
print(day_three_a())
