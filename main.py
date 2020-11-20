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


if __name__ == '__main__':
    # Generating data...
    generate_utilities()
    generate_costs()

    # ... to which we apply multiple voting rules...
    rankings = {"approval": approval_voting(),
                "threshold": threshold_approval_voting(),
                "utility": utility_voting(),
                "cumulative": cumulative_voting(),
                "borda": borda_voting(),
                "knapsack": knapsack_voting()}
    for name, r in rankings.items():
        print(name, ": ", r)

    # ... on which we perform budgeting.
    costs = pd.read_excel(path_costs())
    for name, r in rankings.items():
        print(name, ':\n', knapsack_budgeting(r, costs), "\n")
