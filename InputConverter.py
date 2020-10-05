import random
import pandas as pd

max_utility = 100


def random_utilities(no_voters, no_projects):
    utilities = {}
    for i in range(0, no_projects):
        name = 'project' + str(i)
        utilities[name] = [random.randint(0, max_utility) for i in range(0, no_voters)]
    df = pd.DataFrame(utilities, columns=['project' + str(i) for i in range(0, no_projects)])
    df.to_excel('/home/imme/Documents/AI/Bachelor year 4/Bachelor project/input/test2.xlsx', index=False, header=True)


def approval(no_voters, no_projects, input):
    output_list = []
    for voter in range(0, no_voters):
        voter_list = []
        threshold = random.randint(max_utility/2, max_utility)
        # threshold = 50
        for project in range(0, no_projects):
            result = 1 if input.iloc[voter][project] >= threshold else 0
            voter_list.append(result)
        output_list.append(voter_list)
    # print(output_list)
    return output_list

def approval_counting(no_voters, no_projects, votes):
    projects = no_projects * [0]
    for voter in range(0, no_voters):
        for project in range(0, no_projects):
            projects[project] += votes[voter][project]
    print(projects)

if __name__ == '__main__':
    no_voters = 15
    no_projects = 7
    random_utilities(no_voters, no_projects)
    utilities = pd.read_excel('/home/imme/Documents/AI/Bachelor year 4/Bachelor project/input/test2.xlsx')
    print(utilities)
    approval_counting(no_voters, no_projects, approval(no_voters, no_projects, utilities))
