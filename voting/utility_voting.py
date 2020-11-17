# Author:   Lonneke Pulles

import pandas as pd
from constants import no_projects, path_utilities, path_costs
import xlrd


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

    # A list of tuples, where the first index of the tuple represents the sum of data and the second represents
    # the project number.
    utilities_per_project = [(aggregate['project' + str(i)], i) for i in range(no_projects)]
    utilities_per_project.sort(key=(lambda x: x[0]), reverse=True)
    return [utilities_per_project[i][1] for i in range(no_projects)]


if __name__ == '__main__':
    path = path_utilities()
    utilities = pd.read_excel(path, index_col=0)
    costs = pd.read_excel(path_costs())

    # sums = aggregate_sum(utilities)
    # print(sums)

    utility_dollar_ratio = aggregate_sum_per_cost(utilities, costs)
    print(utility_dollar_ratio)
