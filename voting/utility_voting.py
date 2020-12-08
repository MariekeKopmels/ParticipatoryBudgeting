# Author:   Lonneke Pulles

import pandas as pd
from constants import *


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


def aggregate_product(utility_ballots):
    utility_ballots /= (no_voters * no_projects) # Normalize values s.t. products don't exceed max int.
    aggregate = utility_ballots.product(axis=0)

    # A list of tuples, where the first index of the tuple represents the sum of utilities and the second represents
    # the project number.
    utilities_per_project = [(aggregate['project' + str(i)], i) for i in range(no_projects)]
    utilities_per_project.sort(key=(lambda x: x[0]), reverse=True)
    return [utilities_per_project[i][1] for i in range(no_projects)]


def utility_voting_sum():
    path = path_utilities()
    utilities = pd.read_excel(path, index_col=0)

    sums = aggregate_sum(utilities)
    return sums


def utility_voting_ratio():
    path = path_utilities()
    utilities = pd.read_excel(path, index_col=0)
    costs = pd.read_excel(path_costs())

    utility_dollar_ratio = aggregate_sum_per_cost(utilities, costs)
    return utility_dollar_ratio


def utility_voting_product():
    path = path_utilities()
    utilities = pd.read_excel(path, index_col=0)
    return aggregate_product(utilities)


if __name__ == "__main__":
    print(utility_voting_product())
