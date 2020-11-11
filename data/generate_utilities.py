# This file can generate an excel file contain the data of given number of voters for a
# given number of projects. It generate these data randomly or with Mallow's model.
import random
import pandas as pd
import constants
from constants import no_voters, no_projects, min_utility, max_utility, algorithm, min_cost, max_cost, mallows_p
import openpyxl
import xlrd
import data.mallows as mallows


def utilities_random(filename):
    utilities = {}
    for i in range(0, no_projects):
        name = 'project' + str(i)
        utilities[name] = [random.randint(min_utility, max_utility) for _ in range(0, no_voters)]
    data = pd.DataFrame(utilities,
                        columns=['project' + str(i) for i in range(0, no_projects)])
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
    for i in range(len(probabilities)):
        no_same_rankings = round(probabilities[i] * no_voters)
        for j in range(no_same_rankings):
            # generate utilities and order based on permutations[i]
            random_utilities = [random.randint(min_utility, max_utility) for _ in range(no_projects)]
            random_utilities.sort(reverse=True)
            random_utilities = [(random_utilities[index], index) for index in range(no_projects)]
            random_utilities.sort(key=(lambda x: permutations[i][x[1]]))

            name = 'voter' + str(total_no + j)
            utilities[name] = [random_utilities[idx][0] for idx in range(no_projects)]
        total_no += no_same_rankings
    if total_no != no_voters:
        print('Rounding error. The number of generated votes is not equal to the number of voters.')
    data = pd.DataFrame(utilities,
                        columns=['voter' + str(i) for i in range(0, no_voters)])
    data = data.transpose()
    data.columns = ['project' + str(i) for i in range(no_projects)]
    data.to_excel(filename, index=True, header=True)
    return


if __name__ == '__main__':
    path = constants.path_utilities()

    if algorithm == 'random':
        utilities_random(path)
    elif algorithm == 'mallows':
        utilities_mallow(path)
    else:
        print('Type of algorithm not recognised.')
