# This file can generate an excel file contain the utilities of given number of voters for a
# given number of projects. It generate these utilities randomly or with Mallow's model.
from datetime import datetime
from random import seed, randint, random, shuffle
import pandas as pd

from constants import *
from utilities.mallows import Mallows, spread_voters, all_possible_rankings, pick_random, flip, true_ranking_utilities, some_possible_rankings
from utilities.graph import Graph


def utilities_random(filename):
    utilities = {}
    for i in range(0, no_projects):
        name = 'project' + str(i)
        utilities[name] = [randint(min_utility, max_utility) for _ in range(0, no_voters)]
    data = pd.DataFrame(utilities, columns=['project' + str(i) for i in range(0, no_projects)])
    data.to_excel(filename, index=False, header=True)


def get_permutation():
    permutation = list(range(no_projects))
    shuffle(permutation)
    return permutation


# Get a permutation of a true ranking u that is transitive, i.e. if for projects x, y, z
# it is known that x > y (x is preferred over y) and y > z, then it holds that x > z.
def get_ranking(u):
    graph = Graph(no_projects)

    while True:
        for i in range(0, len(u) - 1):
            for j in range(i + 1, len(u)):
                if random() > mallows_p:  # swap i and j
                    graph.addEdge(u[j], u[i])
                else:                     # keep i and j
                    graph.addEdge(u[i], u[j])

        if not graph.isCyclic():
            break
        else:
            print("throwing away ranking")
            graph = Graph(no_projects)

    return graph.getRanking()


def utilities_mallows(filename):
    utilities = {}

    u = [get_permutation()]
    if opposite_true_rankings:
        u.append(flip(u[0]))
    voters_per_u = spread_voters(2 if opposite_true_rankings else 1)

    start_no = 0
    for true_ranking, voters in zip(u, voters_per_u):
        for v in range(start_no, start_no + voters):
            ranking = get_ranking(true_ranking)

            # Generate utilities and order based on permutations[j].
            random_utilities = [randint(min_utility, max_utility) for _ in range(no_projects)]
            random_utilities.sort(reverse=True)
            random_utilities = [(random_utilities[index], index) for index in range(no_projects)]
            random_utilities.sort(key=(lambda x: ranking[x[1]]))

            # Add result to dictionary 'utilities'.
            name = 'voter' + str(v)
            utilities[name] = [random_utilities[idx][0] for idx in range(no_projects)]
        start_no += voters

    data = pd.DataFrame(utilities, columns=['voter' + str(i) for i in range(0, no_voters)])
    data = data.transpose()
    data.columns = ['project' + str(i) for i in range(no_projects)]
    data.to_excel(filename, index=True, header=True)
    return


def utilities_mallows_inefficient(filename):
    seed(datetime.now())
    # permutations = all_possible_rankings(no_projects)
    permutations = some_possible_rankings(no_projects, no_voters)
    true_rankings = [pick_random(permutations)]
    if opposite_true_rankings:
        true_rankings.append(flip(true_rankings[0]))
        permutations[1] = true_rankings[1]
    permutations[0] = true_rankings[0]
    # print("True rankings: ")
    # print(true_rankings)

    utilities = {}
    start_no = 0
    voters_per_u = spread_voters(2 if opposite_true_rankings else 1)
    # print(voters_per_u)
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
    Path(path_utilities_folder()).mkdir(parents=True, exist_ok=True)
    path = path_utilities()

    if algorithm == 'random':
        utilities_random(path)
    elif algorithm == 'mallows':
        utilities_mallows_inefficient(path)
    else:
        print('Type of algorithm not recognised.')
        exit(1)
