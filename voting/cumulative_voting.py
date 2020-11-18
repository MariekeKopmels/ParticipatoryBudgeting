# Author:   Lonneke Pulles

from constants import path_utilities, path_costs, no_projects
from voting.utility_voting import aggregate_sum, aggregate_sum_per_cost
import pandas as pd


# Returns ballots for every project for every voter.
def cumulative_voting(utilities):
    # Convert utilities to ratios of utilities where the sum per voter is 1.
    aggregate = utilities.aggregate(func=sum, axis='columns')
    return utilities.div(aggregate, axis='rows')


if __name__ == '__main__':
    utilities = pd.read_excel(path_utilities(), index_col=0)
    ballots = cumulative_voting(utilities)

    # Rank projects by sum of votes
    project_ranking = aggregate_sum(ballots)
    print(project_ranking)

    # Rank projects by sum of votes per cost ratio
    costs = pd.read_excel(path_costs())
    project_ranking = aggregate_sum_per_cost(ballots, costs)
    print(project_ranking)
