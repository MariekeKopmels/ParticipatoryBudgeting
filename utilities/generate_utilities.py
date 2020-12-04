# This file can generate an excel file contain the utilities of given number of voters for a
# given number of projects. It generate these utilities randomly or with Mallow's model.
from datetime import datetime
from random import seed, random
import pandas as pd
from constants import *
from utilities.mallows_helper import *


def utilities_random(filename):
    utilities = {}
    for i in range(0, no_projects):
        name = 'project' + str(i)
        utilities[name] = [randint(min_utility, max_utility) for _ in range(0, no_voters)]
    data = pd.DataFrame(utilities, columns=['project' + str(i) for i in range(0, no_projects)])
    data.to_excel(filename, index=False, header=True)


def utilities_mallows(filename):
    seed(datetime.now())
    permutations = all_possible_rankings(no_projects)
    true_rankings = [pick_random(permutations)]
    if opposite_true_rankings:
        true_rankings.append(flip(true_rankings[0]))
    print("True rankings: ")
    print(true_rankings) 

    utilities = {}
    start_no = 0
    voters_per_u = spread_voters(2 if opposite_true_rankings else 1, no_voters)
    print(voters_per_u)
    # Select one or more true rankings.
    for u, voters in zip(true_rankings, voters_per_u):
        utilities.update(true_ranking_utilities(u, permutations, voters, start_no))
        start_no += voters

    # Convert the dictionary 'utilities' into a Pandas DataFrame and store in excel file.
    data = pd.DataFrame(utilities, columns=['voter' + str(i) for i in range(0, no_voters)])
    data = data.transpose()
    data.columns = ['project' + str(i) for i in range(no_projects)]
    data.to_excel(filename, index=True, header=True)
    return


def generate_utilities():
    path = path_utilities()

    if algorithm == 'random':
        utilities_random(path)
    elif algorithm == 'mallows':
        utilities_mallows(path)
    else:
        print('Type of algorithm not recognised.')
        exit(1)


if __name__ == "__main__":
    generate_utilities()
