# Author: Marieke Kopmels

import random
import pandas as pd
from constants import no_voters, no_projects, min_utility, max_utility, path_utilities, folder

def priority_list(threshold_approval):
    approval_counts = threshold_approval.apply(pd.Series.value_counts)
    print(approval_counts)
    threshold_approval = approval_counts.rank(axis='columns')
    print(threshold_approval)
    lst = threshold_approval.iloc[1]
    lieeeest = lst.tolist()
    lieeeest.sort(key=(lambda x: x[1]))
    print(lieeeest)


def threshold_approval(utilities, thresholds):
    approval = pd.DataFrame(index=['voter' + str(i) for i in range(0, no_voters)], columns=['project' + str(j) for j in range(no_projects)])
    for i in range(0, no_voters):
        thresh = thresholds[i]
        # print('threshold of voter ', i, ' : ', thresh)
        for j in range(0, no_projects):
            approval.iloc[i,j] = utilities.iloc[i, j+1] > thresh
    print('approval: ', approval)
    approval.to_excel(folder + 'threshold_approval.xlsx', index=True, header=True)
    return approval


def generate_thresholds():
    thr = {}
    for i in range(no_voters):
        thr[i] = random.randint(min_utility, max_utility)
    return thr


if __name__ == '__main__':
    path = path_utilities()
    utilities = pd.read_excel(path)
    thresholds = generate_thresholds()
    threshold_approval = threshold_approval(utilities, thresholds)
    priority_list = priority_list(threshold_approval)