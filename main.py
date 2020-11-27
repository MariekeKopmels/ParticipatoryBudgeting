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

from voter_satisfaction.social_welfare_satisfaction import social_welfare_satisfaction
from voter_satisfaction.total_social_welfare_satisfaction import total_social_welfare_satisfaction
from voter_satisfaction.egalitarian_satisfaction import *

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
    rankings_pd = pd.DataFrame(rankings)
    rankings_pd.to_excel(path_ranking())

    # ... on which we perform budgeting.
    costs = pd.read_excel(path_costs())
    approval_pd = pd.DataFrame(index=[key for key in rankings], columns=['project' + str(j) for j in range(no_projects)]) #index=[rankings[0, i] for i in range(14)],
    for name, r in rankings.items():
        approval = knapsack_budgeting(r, costs)
        print(name, ':\n', approval, "\n")
        print('test: ', approval.iloc[0, 0])
        temp = []
        for project in range(no_projects):
            temp.append(approval.iloc[0, project])
        approval_pd.loc[name] = temp
    approval_pd.to_excel(path_approval())

    ranking_keys = [key for key in rankings]

    satisfaction(ranking_keys)
