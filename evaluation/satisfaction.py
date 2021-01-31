import pandas as pd
from constants import no_voters, no_projects, path_approved_projects, path_utilities, path_satisfaction, \
    path_satisfaction_folder
import constants
from pathlib import Path


def add_result_columns(utilities):
    utilities[-1] = max(utilities[:no_voters])
    utilities[-2] = sum(utilities[:no_voters])
    utilities[-3] = min(utilities[:no_voters])


def satisfaction(ranking_keys, run_no):
    approved_projects = pd.read_excel(path_approved_projects(), index_col=1)
    utilities = pd.read_excel(path_utilities(), index_col=0)
    columns = ['voter' + str(j) for j in range(no_voters)]
    columns.append('min')
    columns.append('sum')
    columns.append('max')
    approved_dataframe = pd.DataFrame(index=ranking_keys, columns=columns)
    total_dataframe = pd.DataFrame(index=ranking_keys, columns=columns)

    # For every algorithm
    for algorithm in range(len(ranking_keys)):  # length of rankings dictionary in main
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

    Path(path_satisfaction_folder()).mkdir(parents=True, exist_ok=True)

    with pd.ExcelWriter(path_satisfaction()) as writer:
        approved_dataframe.to_excel(writer, sheet_name='approved')
        total_dataframe.to_excel(writer, sheet_name='total')


def combine_results(ranking_keys):
    columns = list(range(constants.max_runs))
    average_sum = pd.DataFrame(index=ranking_keys, columns=columns)
    average_min = pd.DataFrame(index=ranking_keys, columns=columns)
    average_max = pd.DataFrame(index=ranking_keys, columns=columns)

    # Store the statistics of each voting rule during every run in one DataFrame per statistic (e.g. sum).
    for constants.run_no in range(constants.max_runs):
        data = pd.read_excel(path_satisfaction(), index_col=0)

        average_sum[constants.run_no] = data["sum"]
        average_min[constants.run_no] = data["min"]
        average_max[constants.run_no] = data["max"]

    average_sum = average_sum.transpose()
    average_min = average_min.transpose()
    average_max = average_max.transpose()

    with pd.ExcelWriter(constants.path_combination()) as writer:
        average_sum.to_excel(writer, sheet_name='sum')
        average_min.to_excel(writer, sheet_name='min')
        average_max.to_excel(writer, sheet_name='max')
