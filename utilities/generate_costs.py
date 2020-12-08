from random import betavariate, randint
from constants import path_costs, no_projects, min_cost, max_cost
import pandas as pd


# This function generates numbers between min_cost and max_cost for the specified no_projects.
# It draws from the beta distribution with alpha = 2 and beta = 7.
def generate_costs():
    path = path_costs()
    costs = {}

    # Constants for the beta distribution
    # alpha = 2
    # beta = 7

    for i in range(no_projects):
        name = 'project' + str(i)
        # rand_double = betavariate(alpha, beta)
        # while rand_double == 0:
        #     rand_double = betavariate(alpha, beta)
        # costs[name] = min_cost + rand_double * max_cost
        costs[name] = randint(min_cost, max_cost)
    data = pd.DataFrame(costs, index=[0])
    data.to_excel(path, index=False, header=True)


if __name__ == "__main__":
    generate_costs()

