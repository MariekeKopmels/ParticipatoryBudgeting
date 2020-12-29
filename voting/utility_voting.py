# Author:   Lonneke Pulles

import pandas as pd
from constants import *
from math import sqrt


# Returns a list of projects, sorted by decreasing voter preference per project cost.
def aggregate_sum_per_cost(utility_ballots, costs):
    sums = utility_ballots.aggregate(func=sum, axis='rows')
    aggregate = sums / costs.iloc[0]
    project_list = [(aggregate.iloc[i], i) for i in range(no_projects)]
    project_list.sort(key=(lambda x: x[0]), reverse=True)
    return [project_list[i][1] for i in range(no_projects)]


# Returns a list of projects, sorted by decreasing voter preference.
def aggregate_sum(utility_ballots):
    aggregate = utility_ballots.aggregate(func=sum, axis='rows')

    # A list of tuples, where the first index of the tuple represents the sum of utilities and the second represents
    # the project number.
    utilities_per_project = [(aggregate['project' + str(i)], i) for i in range(no_projects)]
    utilities_per_project.sort(key=(lambda x: x[0]), reverse=True)
    return [utilities_per_project[i][1] for i in range(no_projects)]


# Helper function for aggregate product
def valid_product(aggregate):
    for index in range(no_projects):
        if aggregate.iloc[index] == 0:
            return False
    return True


# Returns fraction of elements that lie above zero.
# def balance_above_one(ballots):
#     return (ballots > 1).sum().sum() / (no_projects * no_voters)


def aggregate_product(utility_ballots, cumulative_voting):
    # Normalize values s.t. products don't exceed max int or min int.
    if not cumulative_voting:
        utility_ballots /= sqrt(no_voters)
    else:
        utility_ballots *= no_voters

    # times = 0
    # factor = sqrt(no_voters)
    # while balance_above_one(utility_ballots) > 0.5:  # Most elements have a value above zero.
    #     times -= 1
    #     utility_ballots /= factor
    #
    # while balance_above_one(utility_ballots) < 0.5:  # Most elements have a value below zero.
    #     times += 1
    #     utility_ballots *= factor

    # if cumulative_voting:
    #     utility_ballots *= no_voters

    # print('times: ', times)

    aggregate = utility_ballots.product(axis=0)

    if not valid_product(aggregate):
        print("WARNING: aggregate_product has zero values! Ranking not correct.")

    # A list of tuples, where the first index of the tuple represents the sum of utilities and the second represents
    # the project number.
    utilities_per_project = [(aggregate['project' + str(i)], i) for i in range(no_projects)]
    utilities_per_project.sort(key=(lambda x: x[0]), reverse=True)
    result = [utilities_per_project[i][1] for i in range(no_projects)]
    return result


def utility_voting_sum():
    print("  Utility voting sum")
    path = path_utilities()
    utilities = pd.read_excel(path, index_col=0)

    sums = aggregate_sum(utilities)
    return sums


def utility_voting_ratio():
    print("  Utility voting ratio")
    path = path_utilities()
    utilities = pd.read_excel(path, index_col=0)
    costs = pd.read_excel(path_costs())

    utility_dollar_ratio = aggregate_sum_per_cost(utilities, costs)
    return utility_dollar_ratio


def utility_voting_product():
    print("  Utility voting product")
    path = path_utilities()
    utilities = pd.read_excel(path, index_col=0)
    return aggregate_product(utilities, False)


if __name__ == "__main__":
    pass

