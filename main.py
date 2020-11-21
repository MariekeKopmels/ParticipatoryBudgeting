from data.generate_costs import generate_costs
from data.generate_utilities import *
from voting.approval_voting import approval_voting
from voting.knapsack_voting import knapsack_voting, knapsack_voting_ratio
from voting.threshold_approval_voting import threshold_approval_voting
from voting.utility_voting import utility_voting_sum, utility_voting_ratio
from voting.cumulative_voting import cumulative_voting_sum, cumulative_voting_ratio
from budgeting.knapsack_budgeting import knapsack_budgeting
from voting.borda import borda_voting
from voting.borda import dowdall_system_voting
from voting.borda import euro_song_contest_voting

from constants import *


if __name__ == '__main__':
    # Generating data...
    generate_utilities()
    generate_costs()

    # ... to which we apply multiple voting rules...
    rankings = {"approval": approval_voting(),
                "threshold": threshold_approval_voting(),
                "utility sum": utility_voting_sum(),
                "utility ratio": utility_voting_ratio(),
                "cumulative sum": cumulative_voting_sum(),
                "cumulative ratio": cumulative_voting_ratio(),
                "knapsack": knapsack_voting(),
                "knapsack ratio": knapsack_voting_ratio(),
                "default borda": borda_voting(),
                "default borda truncated": borda_voting(3),
                "dowdall system borda": dowdall_system_voting(),
                "dowdall system borda truncated": dowdall_system_voting(3),
                "eurovision song contest borda": euro_song_contest_voting(),
                "eurovision song contest borda truncated": euro_song_contest_voting(3)}
    for name, r in rankings.items():
        print(name, ": ", r)

    # ... on which we perform budgeting.
    costs = pd.read_excel(path_costs())
    for name, r in rankings.items():
        print(name, ':\n', knapsack_budgeting(r, costs), "\n")
