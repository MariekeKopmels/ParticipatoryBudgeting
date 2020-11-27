import pandas as pd
from constants import *

def total_social_welfare_satisfaction(ranking_keys):
    approved_projects = pd.read_excel(path_approved_projects(), index_col=1)
    utilities = pd.read_excel(path_utilities(), index_col=0)
    columns = ['project' + str(j) for j in range(no_projects)]
    
    columns.append('total utility')
    utility_dataframe = pd.DataFrame(index=ranking_keys, columns=columns)

    # For every algorithm
    for algorithm in range(len(ranking_keys)): # length of rankings dictionary in main
        # print(approved_projects.iloc[algorithm][0] + ':')
        utils = (no_projects + 1) * [0]
        # Calculate for every project the total utility
        for project in range(0, no_projects):
            # print(approved_projects.iloc[algorithm][project])
            # By adding up utilities of voters for each approved project
            for voter in range(no_voters):
                if approved_projects.iloc[algorithm][project]:
                    utils[project] += utilities.iloc[voter][project]
                else:
                    utils[project] -= utilities.iloc[voter][project]
        utils[-1] = sum(utils)
        utility_dataframe.loc[ranking_keys[algorithm]] = utils

    utility_dataframe.to_excel(path_satisfaction('total_social_welfare'))