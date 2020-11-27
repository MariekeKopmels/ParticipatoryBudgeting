from random import randint
from constants import path_costs, no_projects, min_cost, max_cost
import pandas as pd

def generate_costs():
    path = path_costs()
    costs = {}
    for i in range(no_projects):
        name = 'project' + str(i)
        costs[name] = randint(min_cost, max_cost)
    data = pd.DataFrame(costs, index=[0])
    data.to_excel(path, index=False, header=True)

#
# if __name__ == "__main__":
#     generate_costs()
