from random import betavariate, randint
from constants import path_costs, no_projects, min_cost, max_cost, budget, cost_distribution
import numpy as np
import pandas as pd


def valid_costs(costs):
    if sum(costs.values()) == 0 or sum(costs.values()) <= budget:
        return False
    return True


# This function generates numbers between min_cost and max_cost for the specified no_projects.
# It draws from the beta distribution with alpha = 2 and beta = 7.
def generate_costs_betavariate():
    path = path_costs()
    costs = {}

    # Constants for the beta distribution
    alpha = 1.5
    beta = 4

    while not valid_costs(costs):
        for i in range(no_projects):
            name = 'project' + str(i)
            rand_double = betavariate(alpha, beta)
            while rand_double == 0:
                rand_double = betavariate(alpha, beta)
            costs[name] = min_cost + rand_double * max_cost
    data = pd.DataFrame(costs, index=[0])
    data.to_excel(path, index=False, header=True)


def generate_costs_gaussian():
    path = path_costs()
    costs = {}

    # Constants for the beta distribution
    mean = (min_cost + max_cost) / 2
    sigma = (max_cost - min_cost) / 6

    while not valid_costs(costs):
        dist = np.random.normal(mean, sigma, no_projects)
        for i in range(no_projects):
            name = 'project' + str(i)
            costs[name] = dist[i]
    data = pd.DataFrame(costs, index=[0])
    data.to_excel(path, index=False, header=True)


def generate_costs():
    if cost_distribution == 'betavariate':
        return generate_costs_betavariate()
    elif cost_distribution == 'gaussian':
        return generate_costs_gaussian()
    else:
        print("please define cost distribution in constants.py")
        exit()
