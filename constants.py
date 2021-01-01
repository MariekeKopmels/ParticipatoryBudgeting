# This file contains the constants used throughout the project.
from pathlib import Path

# General data constants
no_voters = 50
no_projects = 25

# Utilities constants
algorithm = 'mallows'
min_utility = 1     # of a voter
max_utility = 100    # of a voter

# Money constants
# Note: cost of all projects combined must always be higher than budget
min_cost = 200     # of a project
max_cost = 5000     # of a project
budget = 1000
cost_distribution = 'betavariate'  # either 'betavariate' or 'gaussian'

# Mallows constants
mallows_p = 0.6
opposite_true_rankings = True
division = 0.5

# Run number
max_runs = 1
run_no = 0

# The folder in which the results will be stored on your computer.
folder = str(Path(Path().absolute())) + '/results/' +\
         'voters=' + str(no_voters) +\
         '_projects=' + str(no_projects) +\
         '_true-rankings=' + str(2 if opposite_true_rankings else 1) +\
         '_runs=' + str(max_runs) +\
         '_costs-dist=' + cost_distribution +\
         '/'


def path_utilities():
    return folder + 'utilities/run_no=' + str(run_no) + '.xlsx'


def path_utilities_folder():
    return folder + 'utilities/'


def path_costs():
    return folder + 'utilities/costs.xlsx'


def path_ranking():
    return folder + 'ranking.xlsx'


def path_budget():
    return folder + 'budget.xlsx'


def path_approved_projects():
    return folder + 'approved_voters.xlsx'


def path_satisfaction():
    return path_satisfaction_folder() + '/run_no=' + str(run_no) + '.xlsx'


def path_satisfaction_folder():
    return folder + 'satisfaction/'


def path_combination():
    return path_satisfaction_folder() + 'combined_results.xlsx'
