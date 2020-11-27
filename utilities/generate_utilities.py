# This file can generate an excel file contain the utilities of given number of voters for a
# given number of projects. It generate these utilities randomly or with Mallow's model.
import random
import pandas as pd
from constants import *
import openpyxl
import xlrd
import utilities.mallows as mallows
from datetime import datetime


def utilities_random(filename):
    utilities = {}
    for i in range(0, no_projects):
        name = 'project' + str(i)
        utilities[name] = [random.randint(min_utility, max_utility) for _ in range(0, no_voters)]
    data = pd.DataFrame(utilities, columns=['project' + str(i) for i in range(0, no_projects)])
    data.to_excel(filename, index=False, header=True)


# Generates a file of utilities per voter for every project using Mallows' model.
def utilities_mallow(filename):
    p = mallows_p
    permutations = mallows.all_possible_rankings(no_projects)
    u = mallows.pick_random(permutations)  # Generates one true ranking for a given number of projects.

    probabilities = len(permutations) * [0]
    for i, v in enumerate(permutations):
        probabilities[i] = mallows.mallows_model(v, u, p, no_projects, permutations)
    # print(probabilities)
    # print(sum(probabilities))
    # print(permutations)

    utilities = {}
    total_no = 0
    random.seed(datetime.now())

    for i in range(no_voters):
        num = random.random()
        sum = probabilities[0]
        j = 0
        while num > sum:
            sum += probabilities[j]
            j += 1
        # generate utilities and order based on permutations[j]
        random_utilities = [random.randint(min_utility, max_utility) for _ in range(no_projects)]
        random_utilities.sort(reverse=True)
        random_utilities = [(random_utilities[index], index) for index in range(no_projects)]
        random_utilities.sort(key=(lambda x: permutations[j][x[1]]))

        name = 'voter' + str(i)
        utilities[name] = [random_utilities[idx][0] for idx in range(no_projects)]
    data = pd.DataFrame(utilities, columns=['voter' + str(i) for i in range(0, no_voters)])
    data = data.transpose()
    data.columns = ['project' + str(i) for i in range(no_projects)]
    data.to_excel(filename, index=True, header=True)
    return


# if __name__ == '__main__':
def generate_utilities():
    path = path_utilities()

    if algorithm == 'random':
        utilities_random(path)
    elif algorithm == 'mallows':
        utilities_mallow(path)
    else:
        print('Type of algorithm not recognised.')
