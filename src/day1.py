import os
import math


def get_data():
    current_dir = os.getcwd()
    df = 'day1_data'

    # get data
    f = open(current_dir + '/data/{}'.format(df))
    masses = f.readlines()
    return masses


def day_one_a():
    masses = get_data()
    fuel = 0
    for i in range(len(masses)):
        masses[i] = masses[i].replace("\n", "")
        masses[i] = int(masses[i])
        fuel = fuel + (math.floor(masses[i] / 3) - 2)

    return fuel


def day_one_b():
    masses = get_data()
    fuel = 0
    for i in range(len(masses)):
        masses[i] = masses[i].replace("\n", "")
        masses[i] = int(masses[i])

        # divide new fuel if >= 0

        fuel = fuel + day_one_b_recursive_sum(math.floor(masses[i] / 3) - 2)
    return fuel


def day_one_b_recursive_sum(n):
    if n < 0:
        return 0
    else:
        return n + day_one_b_recursive_sum(math.floor(n/3)-2)
