import random
import pandas as pd

max_utility = 100
no_voters = 100
no_projects = 5


def random_utilities():
    utilities = {}
    for i in range(0, no_projects):
        name = 'project' + str(i)
        utilities[name] = [random.randint(0, max_utility) for i in range(0, no_voters)]
    df = pd.DataFrame(utilities, columns=['project' + str(i) for i in range(0, no_projects)])
    df.to_excel('/home/imme/Documents/AI/Bachelor year 4/Bachelor project/input/test2.xlsx', index=False, header=True)

def ranked_list(input):
    output_list = []
    for voter in range(no_voters):
        # Create list of utilities per voter per project
        voter_utils = []
        for project in range(no_projects):
            voter_utils.append(input.iloc[voter][project + 1])

        voter_ranks = no_projects * [0]
        for project in range(no_projects):
            idx = voter_utils.index(max(voter_utils))
            voter_utils[idx] = -1
            voter_ranks[idx] = project

        voter_ranked_list = no_projects * [0]
        for rank in range(no_projects):
            idx = voter_ranks.index(min(voter_ranks))
            voter_ranked_list[rank] = idx
            voter_ranks[idx] = 999
        output_list.append(voter_ranked_list)
    print(output_list)
    return output_list

# This function is used to order the projects after 
# votes have been counted
# Returns list of projects in ordered from most to
# least points
def order_results(results):
    ordered_results = no_projects * [0]
    for project in range(no_projects):
        maxidx = results.index(max(results))
        ordered_results[project] = maxidx
        results[maxidx] = -999
    # print(ordered_results)
    return ordered_results

# Default borda implementation
def default_borda(votes, vote_length = no_projects):
    results = no_projects * [0]
    for project in range(vote_length):
        points = no_projects - project
        for voter in range(no_voters):
            results[votes[voter][project]] += points
    return results

# Dowdall System implementation. This version of Borda
# favours high preferences
def dowdall_system(votes, vote_length = no_projects):
    results = no_projects * [0]
    for project in range(vote_length):
        points = 1 / (project + 1)
        for voter in range(no_voters):
            results[votes[voter][project]] += points
    return results

def euro_song_contest(votes, vote_length = no_projects):
    results = no_projects * [0]
    for project in range(vote_length):
        if project == 0:
            points = 12
        elif project == 1:
            points = 10
        elif project > 1 and project < 10:
            points = 10 - project
        else:
            points = 0
        for voter in range(no_voters):
            results[votes[voter][project]] += points
    return results

if __name__ == '__main__':
    # random_utilities()
    # utilities = pd.read_excel('/home/imme/Documents/AI/Bachelor year 4/Bachelor project/input/test2.xlsx')
    utilities = pd.read_excel('/home/imme/Documents/AI/Bachelor year 4/Bachelor project/github/ParticipatoryBudgeting/data/mallows_utilities_voters=100_projects=5.xlsx')
    # print(utilities)
    ranked_votes = ranked_list(utilities)

    default = default_borda(ranked_votes)
    dowdall = dowdall_system(ranked_votes)
    euro = euro_song_contest(ranked_votes)

    print(order_results(default))
    print(order_results(dowdall))
    print(order_results(euro))