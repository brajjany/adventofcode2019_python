from helpers import get_data_comma


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
    input_data = get_data_comma(data='day2_data', is_int=1)[0]
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
