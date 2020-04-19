from helpers import get_data_comma


def get_coordinates(init, data):
    """return dict of lines with coordinates, i.e. {line1 : [(x_1,y_1), (x_2,y_2)], line2 : [(x_2,y_2),(x_3,y_3]}"""
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
            raise Exception("Something went wrong.")

        if "Line" + str(i) not in lines.keys():
            lines["Line" + str(i)] = (first_coordinates, second_coordinates)
        else:
            raise Exception("Something went wrong.")

        first_coordinates = second_coordinates

    return lines


def get_line_intersection(line1, line2):
    """
    Returns the distance and intersection given two lines.

    Input:
    line1 ((x1,y1), (x2,y2))
    line2 ((x3,y3), (x4,y4))
    """

    def get_deter(a, b):
        """Gets determinant of 2x2 matrix. If determinant = 0 then no or inf no. of intersections"""
        return a[0] * b[1] - a[1] * b[0]

    x_diff = (line1[0][0]-line1[1][0], line2[0][0]-line2[1][0])
    y_diff = (line1[0][1]-line1[1][1], line2[0][1]-line2[1][1])

    div = get_deter(x_diff, y_diff)

    if div == 0:
        return -1, (-1, -1)

    elif div != 0:
        x = ((get_deter(line1[0], line1[1]) * x_diff[1]) -
             (x_diff[0] * get_deter(line2[0], line2[1]))) / div
        y = ((get_deter(line1[0], line1[1]) * y_diff[1]) -
             (y_diff[0] * get_deter(line2[0], line2[1]))) / div

        distance = abs(x-0) + abs(y-0)

        intersection = 0, (x, y)
        return distance, intersection

    else:
        raise Exception("Something wrong")


def day_three_a():
    data = get_data_comma(data='day3_data')
    output = []
    init = (0, 0)

    # Create array of coordinates
    coordinates_a = get_coordinates(init=init, data=data[0])
    coordinates_b = get_coordinates(init=init, data=data[1])

    # Get intersections
    # intersect = get_line_intersection(coordinates_a["Line0"], coordinates_b["Line0"])

    for p in coordinates_a:
        for q in coordinates_b:
            d, inter = get_line_intersection(coordinates_b[q], coordinates_a[p])

            if d == -1:
                continue
            else:
                output.append(inter)

    return 0, coordinates_a, coordinates_b, output


'''
print('R sum {} len {}: {}'.format(sum(day_three_a()[0]), len(day_three_a()[0]), day_three_a()[0]))
print('L sum {} len {}: {}'.format(sum(day_three_a()[1]), len(day_three_a()[1]), day_three_a()[1]))
print('U sum {} len {}: {}'.format(sum(day_three_a()[2]), len(day_three_a()[2]), day_three_a()[2]))
print('D sum {} len {}: {}'.format(sum(day_three_a()[3]), len(day_three_a()[3]), day_three_a()[3]))
print('Values {} | {}'.format(len(day_three_a()[4]),day_three_a()[4]))
print('Directions {} | {}'.format(len(day_three_a()[5]),day_three_a()[5]))

print('ALL {}'.format(len(get_data_comma(data='day3_data')[0])))'''
print(day_three_a()[3])
