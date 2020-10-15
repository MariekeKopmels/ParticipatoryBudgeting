# The base folder where this GitHub project is stored on your computer.
folder = 'C:/Users/lonne/Google Drive/Bachelor AI/2020-2021/Bachelorproject AI/Github/ParticipatoryBudgeting/'
algorithm = 'random'
no_voters = 5
no_projects = 2
min_utility = 0
max_utility = 100


def path():
    return folder + 'utilities/' + algorithm + '_utilities_voters=' + str(no_voters) + '_projects=' + str(no_projects) + '.xlsx'