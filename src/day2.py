import os
import pandas as pd
import numpy as np


def get_data():
    current_dir = os.getcwd()
    df = 'day2_data'

    # f = pd.read_csv(current_dir + '/data/{}'.format(df), sep=',')
    f = np.genfromtxt(current_dir + '/data/{}'.format(df), delimiter=',')

    return f.astype(int)


def get_opcode(i, x, y):
    if i == 1:
        return x + y
    elif i == 2:
        return x * y
    else:
        # program halt
        return -9999999


def day_two_a(noun=0, verb=0):
    # init local vars
    input_data = get_data().tolist()
    input_data[1] = noun  # noun
    input_data[2] = verb  # verb
    i = 0

    while i < len(input_data):
        if input_data[i] == 99:
            break
        else:
            input_data[input_data[i + 3]] = get_opcode(input_data[i], input_data[input_data[i + 1]],
                                                       input_data[input_data[i + 2]])
        i = i + 4

    # output, noun, verb
    return input_data[0], input_data[1], input_data[2]


"""
memory = list of integers
address = position in memory
Opcode (1,2,99) is beginning of an instruction
Parameters = values used immediately after an opcode
Current instruction = instruction pointer (init=0), increases by number of values in instruction (always 4, 1 opcode + 3 parameters)
"""


def day_two_b():
    noun_index = 0
    verb_index = 0
    output = -1

    while noun_index < 99:

        while verb_index < 99:
            output, noun, verb = day_two_a(noun_index, verb_index)
            if output == 19690720:
                break
            else:
                verb_index += 1

        if output == 19690720:
            break
        else:
            verb_index = 0
            noun_index += 1

    return output, noun_index, verb_index, 100*noun_index + verb_index
