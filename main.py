from utilities.generate_costs import generate_costs
from utilities.generate_utilities import *
import random
from voting.approval_voting import approval_voting
from voting.knapsack_voting import knapsack_voting, knapsack_voting_ratio
from voting.threshold_approval_voting import threshold_approval_voting
from voting.utility_voting import utility_voting_sum, utility_voting_ratio, utility_voting_product
from voting.cumulative_voting import cumulative_voting_sum, cumulative_voting_ratio, cumulative_voting_product
from voting.borda import get_ranked_list
from voting.borda import borda_voting
from voting.borda import dowdall_system_voting
from voting.borda import euro_song_contest_voting


from budgeting.knapsack_budgeting import knapsack_budgeting

from results.satisfaction import *

import constants


def main_function():
    # # Generating utilities...
    random.seed(datetime.now())
    generate_utilities()
    generate_costs()
    print("Generated utilities")

    print("Starting voting algorithms...")

    ranked_votes = get_ranked_list()

    # print('run_no now is ', constants.run_no)
    # ... to which we apply multiple voting rules...
    rankings = {"approval": approval_voting(),
                "threshold": threshold_approval_voting(),
                "utility sum": utility_voting_sum(),
                "utility ratio": utility_voting_ratio(),
                "utility product": utility_voting_product(),
                "cumulative sum": cumulative_voting_sum(),
                "cumulative ratio": cumulative_voting_ratio(),
                "cumulative product": cumulative_voting_product(),
                "knapsack": knapsack_voting(),
                "knapsack ratio": knapsack_voting_ratio(),
                "default borda": borda_voting(ranked_votes),
                "default borda truncated": borda_voting(ranked_votes, vote_length = 8),
                "dowdall system borda": dowdall_system_voting(ranked_votes),
                "dowdall system borda truncated": dowdall_system_voting(ranked_votes, vote_length = 8),
                "eurovision song contest borda": euro_song_contest_voting(ranked_votes),
                "eurovision song contest borda truncated": euro_song_contest_voting(ranked_votes, vote_length = 8)}

    print("Finished algorithms")

    # for name, r in rankings.items():
    #     print(name, ": ", r)
    rankings_pd = pd.DataFrame(rankings)
    rankings_pd.to_excel(path_ranking())

    # rankings = pd.read_excel(path_ranking(), index_col=0)
    # print(rankings)


    print("Applying budgeting...")
    # ... on which we perform budgeting.
    costs = pd.read_excel(path_costs())
    approval_pd = pd.DataFrame(index=[key for key in rankings], columns=['project' + str(j) for j in range(no_projects)]) #index=[rankings[0, i] for i in range(14)],
    for name, r in rankings.items():
        approval = knapsack_budgeting(r, costs)
        # print(name, ':\n', approval, "\n")
        # print('test: ', approval.iloc[0, 0])
        temp = []
        for project in range(no_projects):
            temp.append(approval.iloc[0, project])
        approval_pd.loc[name] = temp
    approval_pd.to_excel(path_approved_projects())

    ranking_keys = [key for key in rankings]

    # Finally, evaluate the voters' results with the selected projects.
    print("Evaluating satisfaction...")
    satisfaction(ranking_keys, constants.run_no)
    print("Done.\n")


if __name__ == '__main__':
    for constants.run_no in range(1):
        print("Run: ", constants.run_no)
        main_function()


