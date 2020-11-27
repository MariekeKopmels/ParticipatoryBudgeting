import pandas as pd
from constants import *

def add_result_columns(utilities):
    utilities[-1] = max(utilities[:no_voters])
    utilities[-2] = sum(utilities[:no_voters])
    utilities[-3] = min(utilities[:no_voters])


def satisfaction(ranking_keys):
    approved_projects = pd.read_excel(path_approved_projects(), index_col=1)
    utilities = pd.read_excel(path_utilities(), index_col=0)
    columns = ['voter' + str(j) for j in range(no_voters)]
    columns.append('min')
    columns.append('sum')
    columns.append('max')
    approved_dataframe = pd.DataFrame(index=ranking_keys, columns=columns)
    total_dataframe = pd.DataFrame(index=ranking_keys, columns=columns)

    # For every algorithm
    for algorithm in range(len(ranking_keys)): # length of rankings dictionary in main
        # Create list of utilities for every voter
        approved_utils = (no_voters + 3) * [0]
        total_utils = (no_voters + 3) * [0]

        for voter in range(no_voters):
            for project in range(no_projects):
                # Count only approved projects
                if approved_projects.iloc[algorithm][project]:
                    approved_utils[voter] += utilities.iloc[voter][project]
                    total_utils[voter] += utilities.iloc[voter][project]
                else:
                    total_utils[voter] -= utilities.iloc[voter][project]

        add_result_columns(approved_utils)
        add_result_columns(total_utils)

        approved_dataframe.loc[ranking_keys[algorithm]] = approved_utils
        total_dataframe.loc[ranking_keys[algorithm]] = total_utils

    with pd.ExcelWriter(path_satisfaction('satisfaction')) as writer:
        approved_dataframe.to_excel(writer, sheet_name='approved')
        total_dataframe.to_excel(writer, sheet_name='total')

