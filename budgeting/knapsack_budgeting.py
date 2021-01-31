
from constants import no_projects, path_budget, path_costs, budget
import pandas as pd

def knapsack_budgeting(project_ranking, costs):
    approval = pd.DataFrame(index=['approved', 'unspent money'], columns=['project' + str(j) for j in range(no_projects)])
    budget_left = budget
    for i in range(no_projects):
        project = project_ranking[i]
        approved = costs.iloc[0, project] < budget_left
        approval.iloc[0, project] = approved
        if approved:
            budget_left -= costs.iloc[0, project]
    approval.iloc[1, 0] = budget_left
    filename = path_budget()
    approval.to_excel(filename, index=True, header=True)
    return approval