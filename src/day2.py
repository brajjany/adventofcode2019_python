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


def day_two():
    # init local vars
    input_data = get_data().tolist()
    input_data[1] = 12
    input_data[2] = 2
    i = 0

    while i < len(input_data):
        if input_data[i] == 99:
            break
        else:
            input_data[input_data[i+3]] = get_opcode(input_data[i], input_data[input_data[i+1]], input_data[input_data[i+2]])
        i = i + 4

    return input_data
