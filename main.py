from data.generate_costs import generate_costs
from data.generate_utilities import *
from voting.approval_voting import approval_voting
from voting.knapsack_voting import knapsack_voting
from voting.threshold_approval_voting import threshold_approval_voting
from voting.utility_voting import utility_voting
from voting.cumulative_voting import cumulative_voting
from budgeting.knapsack_budgeting import knapsack_budgeting
from voting.borda import borda_voting
from constants import *

<<<<<<< HEAD
from voting.borda import borda_voting
from voting.borda import truncated_borda_voting
from voting.borda import dowdall_system_voting
from voting.borda import truncated_dowdall_system_voting
from voting.borda import euro_song_contest_voting
from voting.borda import truncated_euro_song_contest_voting

=======
>>>>>>> e6b7075002ac333c5244468f25c3248c361b6d1d

if __name__ == '__main__':
    # Generating data...
    generate_utilities()
    generate_costs()

    # ... to which we apply multiple voting rules...
    rankings = {"approval": approval_voting(),
                "threshold": threshold_approval_voting(),
                "utility": utility_voting(),
                "cumulative": cumulative_voting(),
<<<<<<< HEAD
                "knapsack": knapsack_voting(),
                "default borda": borda_voting(),
                "default borda truncated": truncated_borda_voting(3),
                "dowdall system borda": dowdall_system_voting(),
                "dowdall system borda truncated": truncated_dowdall_system_voting(3),
                "eurovision song contest borda": euro_song_contest_voting(),
                "eurovision song contest borda truncated": truncated_euro_song_contest_voting(3)}

    print(rankings)
=======
                "borda": borda_voting(),
                "knapsack": knapsack_voting()}
    for name, r in rankings.items():
        print(name, ": ", r)
>>>>>>> e6b7075002ac333c5244468f25c3248c361b6d1d

    # ... on which we perform budgeting.
    costs = pd.read_excel(path_costs())
    for name, r in rankings.items():
        print(name, ':\n', knapsack_budgeting(r, costs), "\n")
