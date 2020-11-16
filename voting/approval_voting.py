# This file can generate the approval vote based on the data of voters for certain projects.

import pandas as pd
from constants import no_projects, no_voters, path_utilities
import openpyxl
import xlrd


def approval(input):
    threshold = 50
    booleans = input.transform(lambda x: x >= threshold)
    aggregate = booleans.sum(axis=0).tolist()
    list = [(aggregate[i], i) for i in range(len(aggregate))]
    list.sort(key=(lambda x: x[0]), reverse=True)
    return [x[1] for x in list]


if __name__ == '__main__':
    path = path_utilities()
    utilities = pd.read_excel(path, index_col=0)
    approval_voting = approval(utilities)
    print(approval_voting)

