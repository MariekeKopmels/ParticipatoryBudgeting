# The base folder where this GitHub project is stored on your computer.
folder = 'C:/Users/lonne/Google Drive/Bachelor AI/2020-2021/Bachelorproject AI/Github/ParticipatoryBudgeting/'
algorithm = 'random'
no_voters = 5
no_projects = 2
min_utility = 0
max_utility = 99
min_cost = 0
max_cost = 1000000


def path_utilities():
    return folder + 'data/' + algorithm + '_utilities_voters=' + str(no_voters) + '_projects=' + str(no_projects) + '.xlsx'


def path_costs():
    return folder + 'data/costs_projects=' + str(no_projects) + '.xlsx'

