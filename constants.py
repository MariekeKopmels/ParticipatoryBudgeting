# This file contains the constants used throughout the project.
# For the final results, we use €10k, 10 projecten van €2000-8000, 10k deelnemers.

# The base folder where this GitHub project is stored on your computer.
# folder = 'C:/Users/lonne/Google Drive/Bachelor AI/2020-2021/Bachelorproject AI/Github/ParticipatoryBudgeting/'
# folder = '/Users/remcosteen/Desktop/AI5/BP/Algorithm/ParticipatoryBudgeting/'
folder = '/home/imme/Documents/AI/Bachelor year 4/Bachelor project/github/ParticipatoryBudgeting/'

# General data constants
no_voters = 10  # NB: this shouldn't be lower than 5
no_projects = 6

# Utilities constants
algorithm = 'mallows'
min_utility = 0     # of a voter
max_utility = 99    # of a voter

# Money constants
min_cost = 2000     # of a project
max_cost = 5000     # of a project
budget = 10000

# Mallows constants
mallows_p = 0.6
opposite_true_rankings = True
division = 0.5


def path_utilities():
    return folder + 'utilities/' + algorithm + '_utilities_voters=' + str(no_voters) + '_projects=' + str(
        no_projects) + '.xlsx'


def path_costs():
    return folder + 'utilities/costs_projects=' + str(no_projects) + '.xlsx'


def path_ranking():
    return folder + 'results/ranking_voters=' + str(no_voters) + '_projects=' + str(
        no_projects) + '.xlsx'


def path_budget():
    return folder + 'results/budget_voters=' + str(no_voters) + '_projects=' + str(
        no_projects) + '.xlsx'


def path_approved_projects():
    return folder + 'results/approved_voters=' + str(no_voters) + '_projects=' + str(
        no_projects) + '.xlsx'


def path_satisfaction():
    return folder + 'results/satisfaction_voters=' + str(no_voters) + '_projects=' + str(
        no_projects) + '.xlsx'
