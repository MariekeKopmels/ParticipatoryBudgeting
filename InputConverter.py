# This file

import random
import pandas as pd
import openpyxl
import xlrd

max_utility = 100


def random_utilities(no_voters, no_projects):
    utilities = {}
    for i in range(0, no_projects):
        name = 'project' + str(i)
        utilities[name] = [random.randint(0, max_utility) for i in range(0, no_voters)]
    input = pd.DataFrame(utilities, columns=['project' + str(i) for i in range(0, no_projects)])
    input.to_excel(r'/Users/remcosteen/Desktop/AI5/BP/Code/Output/random_utilities.xlsx', index=False, header=True)


def approval(no_voters, no_projects, input):
    output_list = no_projects*[no_voters*[0]]
    print(output_list)
    # output = pd.DataFrame()
    # output = input.DataFrame(utilities, columns=['project' + str(i) for i in range(0, no_projects)])
    for voter in range(0, no_voters):
        threshold = 50
            # random.randint(int(max_utility / 2), max_utility)
        # print(threshold)
        for project in range(0, no_projects):
            result = 1 if input.iloc[voter][project] >= threshold else 0
            output_list[project][voter] = result
            print('Voter: ' + str(voter) + ' Project: ' + str(project) + ' Result: ' + str(result))
    print(output_list)

if __name__ == '__main__':
    no_voters = 5
    no_projects = 2
    random_utilities(no_voters, no_projects)
    utilities = pd.read_excel('/Users/remcosteen/Desktop/AI5/BP/Code/Output/random_utilities.xlsx')
    print(utilities)
    approval(no_voters, no_projects, utilities)

