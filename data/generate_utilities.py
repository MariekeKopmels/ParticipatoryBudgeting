# This file can generate an excel file contain the data of given number of voters for a
# given number of projects. It generate these data randomly or with Mallow's model.
import random
import pandas as pd
import constants
from constants import no_voters, no_projects, min_utility, max_utility, algorithm, min_cost, max_cost
import openpyxl
import xlrd


def utilities_random(filename):
    utilities = {}
    for i in range(0, no_projects):
        name = 'project' + str(i)
        utilities[name] = [random.randint(min_utility, max_utility) for _ in range(0, no_voters)]
    data = pd.DataFrame(utilities,
                        columns=['project' + str(i) for i in range(0, no_projects)])
    data.to_excel(filename, index=False, header=True)


# TODO use mallows.py to implement this
def utilities_mallow(filename):
    pass


if __name__ == '__main__':
    path = constants.path_utilities()

    if algorithm == 'random':
        utilities_random(path)
    elif algorithm == 'mallows':
        utilities_mallow(path)
    else:
        print('Type of algorithm not recognised.')
