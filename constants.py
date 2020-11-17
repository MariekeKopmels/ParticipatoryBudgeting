# This file contains the constants used throughout the project.
# For the final results, we use €10k, 10 projecten van €2000-8000, 10k deelnemers.

# The base folder where this GitHub project is stored on your computer.
folder = 'C:/Users/lonne/Google Drive/Bachelor AI/2020-2021/Bachelorproject AI/Github/ParticipatoryBudgeting/'
# folder = '/Users/remcosteen/Desktop/AI5/BP/Algorithm/ParticipatoryBudgeting/'
algorithm = 'mallows'
no_voters = 100           # NB: this shouldn't be lower than 5
no_projects = 6
min_utility = 0
max_utility = 99
min_cost = 2000
max_cost = 8000
budget = 10000
mallows_p = 0.6


def path_utilities():
    return folder + 'data/' + algorithm + '_utilities_voters=' + str(no_voters) + '_projects=' + str(no_projects) + '.xlsx'


def path_costs():
    return folder + 'data/costs_projects=' + str(no_projects) + '.xlsx'


def path_budget():
    return folder + 'data/budget.xlsx'