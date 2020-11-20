# Author:   Lonneke Pulles

from constants import *
from voting.utility_voting import aggregate_sum, aggregate_sum_per_cost
import pandas as pd


# Returns ballots for every project for every voter.
def get_ballots(utilities):
    # Convert utilities to ratios of utilities where the sum per voter is 1.
    aggregate = utilities.aggregate(func=sum, axis='columns')
    return utilities.div(aggregate, axis='rows')


def cumulative_voting_sum():
    utilities = pd.read_excel(path_utilities(), index_col=0)
    ballots = get_ballots(utilities)

    # Rank projects by sum of votes
    project_ranking = aggregate_sum(ballots)
    return project_ranking


def cumulative_voting_ratio():
    utilities = pd.read_excel(path_utilities(), index_col=0)
    ballots = get_ballots(utilities)

    # Rank projects by sum of votes per cost ratio
    costs = pd.read_excel(path_costs())
    project_ranking = aggregate_sum_per_cost(ballots, costs)
    return project_ranking
