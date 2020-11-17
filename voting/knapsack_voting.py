# Author: Marieke Kopmels

import pandas as pd
from constants import no_projects, no_voters, path_utilities, path_costs, budget


def get_priority_list(knapsack_approval):
    approval_counts = knapsack_approval.apply(pd.Series.value_counts)
    test = approval_counts.iloc[1]
    test_1 = list(zip(test, test.index))
    test_1.sort(key=(lambda x: x[0]), reverse=True)
    new_list = []
    for el in test_1:
        new_list.append(int(el[1][-1]))
    return new_list


def get_individual_ranking(voter, utilities):
    individual_utilities = utilities.loc[voter]
    # print('individual ranking: ', individual_utilities)
    individual_utilities = individual_utilities.iloc[1:]
    # print(individual_utilities)
    individual_utilities = list(zip(individual_utilities, individual_utilities.index))
    # print(individual_utilities)
    individual_utilities.sort(key=(lambda x:x[0]), reverse=True)
    individual_ranking = []
    for el in individual_utilities:
        individual_ranking.append(int(el[1][-1]))
    return individual_ranking


def get_individual_ratio_ranking(voter, utilities, costs):
    individual_utilities = utilities.loc[voter]
    individual_utilities = individual_utilities.iloc[1:]
    individual_utilities = list(zip(individual_utilities, individual_utilities.index))
    # print(individual_utilities)
    individual_utilities_per_dollar = []
    for project in range (no_projects):
        project_string = 'project' + str(project)
        new_item = tuple((int(individual_utilities[project][0]) / costs.iloc[0, project], project_string))
        individual_utilities_per_dollar.append(new_item)
    # print(individual_utilities_per_dollar)
    individual_utilities_per_dollar.sort(key=(lambda x:x[0]), reverse=True)
    # print(individual_utilities_per_dollar)
    individual_ranking = []
    for el in individual_utilities_per_dollar:
        individual_ranking.append(int(el[1][-1]))
    return individual_ranking


# returns dataframe, with true or false for approval of projects per voter.
def knapsack_approval(utilities, costs):
    approval = pd.DataFrame(index=['voter' + str(i) for i in range(no_voters)], columns=['project' + str(j) for j in range(no_projects)])
    for i in range(no_voters):
        budget_left = budget
        # print('initial budget: ', budget_left)
        individual_ranked_list = get_individual_ranking(i, utilities)
        # print('ranked list of voter ', i, ': ', individual_ranked_list)
        # print(costs)
        for j in range(no_projects):
            current_project = individual_ranked_list[j]
            approved = costs.iloc[0, current_project] < budget_left
            approval.iloc[i, current_project] = approved
            if approved:
                budget_left -= costs.iloc[0, current_project]
            # print('current approval: \n', approval.iloc[i])
            # print('budget left: ', budget_left)
    return approval


# returns dataframe, with true or false for approval of projects per voter.
def knapsack_approval_ratio(utilities, costs):
    approval = pd.DataFrame(index=['voter' + str(i) for i in range(no_voters)], columns=['project' + str(j) for j in range(no_projects)])
    for i in range(no_voters):
        budget_left = budget
        # print('initial budget: ', budget_left)
        individual_ranked_list = get_individual_ratio_ranking(i, utilities, costs)
        # print('ranked list of voter ', i, ': ', individual_ranked_list)
        # print(costs)
        for j in range(no_projects):
            current_project = individual_ranked_list[j]
            approved = costs.iloc[0, current_project] < budget_left
            approval.iloc[i, current_project] = approved
            if approved:
                budget_left -= costs.iloc[0, current_project]
            # print('current approval: \n', approval.iloc[i])
            # print('budget left: ', budget_left)
    return approval


if __name__ == '__main__':
    path_utilities = path_utilities()
    utilities = pd.read_excel(path_utilities)
    path_costs = path_costs()
    costs = pd.read_excel(path_costs)

    knapsack_approval = knapsack_approval(utilities, costs)
    priority_list = get_priority_list(knapsack_approval)
    print('priority list: ', priority_list)

    knapsack_approval_ratio = knapsack_approval_ratio(utilities, costs)
    priority_list_ratio = get_priority_list(knapsack_approval_ratio)
    print('ratio priority list: ', priority_list_ratio)

