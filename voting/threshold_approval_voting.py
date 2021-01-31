# Author: Marieke Kopmels

import random
import pandas as pd
from constants import *


# Helper function, returns a priority list of all project, based on which project was approved by most of the voters,
# i.e. the project with the most votes is no. 1, the project with the second most votes no. 2, etc.
def generate_priority_list(threshold_approval):
    approval_counts = threshold_approval.apply(pd.Series.value_counts)
    votes_per_project = approval_counts.iloc[1]
    list_votes_per_project = list(zip(votes_per_project, votes_per_project.index))
    list_votes_per_project.sort(key=(lambda x: x[0]), reverse=True)
    priority_list = []
    for el in list_votes_per_project:
        priority_list.append(int(el[1][7:]))
    return priority_list


# Helper function returns a dataframe containing a schema stating which voter approved which projects,
# based on it's threshold and utility for a certain project.
def generate_threshold_approval(utilities, thresholds):
    approval = pd.DataFrame(index=['voter' + str(i) for i in range(0, no_voters)], columns=['project' + str(j) for j in range(no_projects)])
    for i in range(0, no_voters):
        thresh = thresholds[i]
        for j in range(0, no_projects):
            approval.iloc[i,j] = utilities.iloc[i, j+1] > thresh
    return approval


# Helper function, returns a dictionary containing a randomly generated threshold, between the minimal and
# maximum utility, per voter.
def generate_thresholds():
    thr = {}
    for i in range(no_voters):
        thr[i] = random.randint(min_utility, max_utility)
    return thr


# The main function, performs threshold approval voting.
def threshold_approval_voting():
    print("  Threshold approval voting")
    path = path_utilities()
    utilities = pd.read_excel(path)
    thresholds = generate_thresholds()
    threshold_approval = generate_threshold_approval(utilities, thresholds)
    priority_list = generate_priority_list(threshold_approval)
    return priority_list
