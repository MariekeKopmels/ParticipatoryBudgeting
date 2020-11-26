import pandas as pd
from constants import *

def social_welfare_satisfaction(ranking_keys):
    approved_projects = pd.read_excel(path_approved_projects())
    utilities = pd.read_excel(path_utilities())

    utility_dataframe = pd.DataFrame(index=ranking_keys, columns=['project' + str(j) for j in range(no_projects)])

    # For every algorithm
    for algorithm in range(len(ranking_keys)): # length of rankings dictionary in main
        # print(approved_projects.iloc[algorithm][0] + ':')
        utils = no_projects * [0]
        # Calculate for every project the total utility
        for project in range(1, no_projects + 1):
            # print(approved_projects.iloc[algorithm][project])
            if approved_projects.iloc[algorithm][project]:
                # By adding up utilities of voters for each approved project
                for voter in range(no_voters):
                    utils[project - 1] += utilities.iloc[voter][project]
        utility_dataframe.loc[ranking_keys[algorithm]] = utils

    utility_dataframe.to_excel(path_welfare_satisfaction())


        