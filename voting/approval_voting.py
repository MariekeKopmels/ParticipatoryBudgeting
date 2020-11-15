# This file can generate the approval vote based on the data of voters for certain projects.

import pandas as pd
from constants import no_projects, no_voters, path_utilities
import openpyxl
import xlrd


def approval(input):
    threshold = 50
    print(type(input))
    approval = {}
    for i in range(0,no_voters):
        print(input.iloc[i,1])
    return 5 #input.transform(lambda x: x >= threshold)
    # Alternative implementation (returns list instead of pandas dataframe)
    #
    # output_list = no_projects*[no_voters*[0]]
    #     print(output_list)
    #     # output = pd.DataFrame()
    #     # output = input.DataFrame(data, columns=['project' + str(i) for i in range(0, no_projects)])
    #     for voter in range(0, no_voters):
    #         threshold = 50
    #             # random.randint(int(max_utility / 2), max_utility)
    #         # print(threshold)
    #         for project in range(0, no_projects):
    #             result = 1 if input.iloc[voter][project] >= threshold else 0
    #             output_list[project][voter] = result
    #             print('Voter: ' + str(voter) + ' Project: ' + str(project) + ' Result: ' + str(result))
    #     print(output_list)


if __name__ == '__main__':
    path = path_utilities()
    utilities = pd.read_excel(path)
    approval_voting = approval(utilities)
    print(approval_voting)

