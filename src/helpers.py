import os
import pandas as pd
import csv


def get_data_comma(data, is_int=0):
    current_dir = os.getcwd()
    results = []
    # f = np.genfromtxt(current_dir + '/data/{}'.format(data), delimiter=delimiter)
    # f = pd.read_csv(current_dir + '/data/{}'.format(data))
    with open(current_dir + '/data/{}'.format(data)) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            results.append(row)

    if is_int:
        for i in range(len(results)):
            results[i] = [int(j) for j in results[i]]

    return results
