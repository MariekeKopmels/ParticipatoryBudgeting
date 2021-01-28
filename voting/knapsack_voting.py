# Author: Marieke Kopmels

import pandas as pd
from constants import *


# Helper function, returns a priority list of all project, based on which project was approved by most of the voters,
# i.e. the project with the most votes is no. 1, the project with the second most votes no. 2, etc.
def generate_priority_list(knapsack_approval):
    # print('knapsack approval: ', knapsack_approval)
    approval_counts = knapsack_approval.apply(pd.Series.value_counts)
    # TODO: Crashes when all projects combined are within budget
    votes_per_project = approval_counts.iloc[1]
    list_votes_per_project = list(zip(votes_per_project, votes_per_project.index))
    list_votes_per_project.sort(key=(lambda x: x[0]), reverse=True)
    priority_list = []
    for el in list_votes_per_project:
        priority_list.append(int(el[1][7:]))
    return priority_list


# Returns the ranking of projects for a certain voter.
def generate_individual_ranking(voter, utilities):
    individual_utilities = utilities.loc[voter]
    individual_utilities = individual_utilities.iloc[1:]
    individual_utilities = list(zip(individual_utilities, individual_utilities.index))
    individual_utilities.sort(key=(lambda x:x[0]), reverse=True)
    individual_ranking = []
    # print(individual_utilities)
    for el in individual_utilities:
        individual_ranking.append(int(el[1][7:]))
        # print(individual_ranking)
    return individual_ranking


# Returns the ranking of projects for a certain voter, taking the costs of a project into account.
def generate_individual_ratio_ranking(voter, utilities, costs):
    individual_utilities = utilities.loc[voter]
    individual_utilities = individual_utilities.iloc[1:]
    individual_utilities = list(zip(individual_utilities, individual_utilities.index))
    individual_utilities_per_dollar = []
    for project in range (no_projects):
        project_string = 'project' + str(project)
        new_item = tuple((int(individual_utilities[project][0]) / costs.iloc[0, project], project_string))
        individual_utilities_per_dollar.append(new_item)
    individual_utilities_per_dollar.sort(key=(lambda x:x[0]), reverse=True)
    individual_ranking = []
    for el in individual_utilities_per_dollar:
        individual_ranking.append(int(el[1][7:]))
    return individual_ranking


# returns dataframe, with true or false for approval of projects per voter.
def generate_knapsack_approval(utilities, costs):
    approval = pd.DataFrame(index=['voter' + str(i) for i in range(no_voters)], columns=['project' + str(j) for j in range(no_projects)])
    for i in range(no_voters):
        budget_left = budget
        individual_ranked_list = generate_individual_ranking(i, utilities)
        for j in range(no_projects):
            current_project = individual_ranked_list[j]
            approved = costs.iloc[0, current_project] < budget_left
            approval.iloc[i, current_project] = approved
            if approved:
                budget_left -= costs.iloc[0, current_project]
    return approval


# returns dataframe, with true or false for approval of projects per voter, taking the cost of a project into account.
def generate_knapsack_approval_ratio(utilities, costs):
    approval = pd.DataFrame(index=['voter' + str(i) for i in range(no_voters)], columns=['project' + str(j) for j in range(no_projects)])
    for i in range(no_voters):
        budget_left = budget
        individual_ranked_list = generate_individual_ratio_ranking(i, utilities, costs)
        for j in range(no_projects):
            current_project = individual_ranked_list[j]
            approved = costs.iloc[0, current_project] < budget_left
            approval.iloc[i, current_project] = approved
            if approved:
                budget_left -= costs.iloc[0, current_project]
    return approval


# The first main function, performs knapsack voting.
def knapsack_voting():
    print("  Knapsack voting")
    path_util = path_utilities()
    utilities = pd.read_excel(path_util)
    path_c = path_costs()
    costs = pd.read_excel(path_c)
    approval = generate_knapsack_approval(utilities, costs)
    ranking = generate_priority_list(approval)
    return ranking


# The second main function, performs knapsack voting based on the cost of a project, so per ratio.
def knapsack_voting_ratio():
    print("  Knapsack voting ratio")
    path_util = path_utilities()
    utilities = pd.read_excel(path_util)
    path_c = path_costs()
    costs = pd.read_excel(path_c)
    approval = generate_knapsack_approval_ratio(utilities, costs)
    ranking_ratio = generate_priority_list(approval)
    return ranking_ratio

