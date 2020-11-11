# This file generates a probability distribution of ballots using the Mallows noise model: a noise model
# for rankings, i.e. an r-noise model over a candidate set A. This is a family of probability distributions
# that assign a probability to each possible ranking of all alternatives (here: projects).
#
# Definitions (based on the book):
# A: the candidate set, i.e. the set of options (=alternatives; here: projects) to vote on. |A| >= 2.
# p: the probability that a voter correctly identifies the better alternative given two options.
# u: the true state of the world; the true ranking.
# v: a ranking that agrees with u on k pairs of alternatives
# k: the number of pairs of alternatives that v agrees on with u, the true state of the world, i.e.
#    the number of pairs in which the voter has chosen the better of the two alternatives
# m: |A|, aka no_projects.
# d_swap: (m choose 2) - k. The number of pairs that v doesn't contain or that don't agree with u.
# phi: p/(1-p)
#
# Assumptions:
# The number of and differences between voters is ignored. As a result, we simply assume that each voter
# has the same probability p of choosing the better alternative.

from datetime import datetime
import random
import itertools


# # Returns the combination (nCr): the number of ways in which r elements can be chosen from n objects.
# def ncr(n, r):
#     r = min(r, n-r)
#     numer = reduce(op.mul, range(n, n-r, -1), 1)
#     denom = reduce(op.mul, range(1, r+1), 1)
#     return numer // denom


# Generates all possible rankings for a given number of projects.
def all_possible_rankings(no_projects):
    basis = list(range(no_projects))
    return list(itertools.permutations(basis))


def pick_random(permutations):
    return permutations[random.randint(0, len(permutations)-1)]


# Returns the swap distance: the number of elements one should swap in one ranking to obtain
# the other. Formally, the number of pairs (c, c′) ∈ A × A such that u ranks c above c′, but v
# ranks c′ above c.
# Can also be calculated with: nCr(no_projects, 2) - k, where k is the number of rankings u and v
# agree on.
# FIXME
def d_swap(v, u, no_projects):
    count = 0
    for i in range(no_projects-1):
        for j in range(i+1, no_projects):
            if (v.index(i) > v.index(j)) != (u.index(i) > u.index(j)):
                # u and v do not agree on the ranking of alternatives i and j.
                count += 1
    return count
    # return 0


# Returns mu_p, where mu_p is the sum over all possible rankings v given a set of projects
# of phi ** (- d_swap(v,u))
def get_mu_p(u, phi, no_projects, all_possible_v):
    sum = 0
    for v in all_possible_v:
        sum += phi ** (-d_swap(v, u, no_projects))
    return sum


def mallows_model(v, u, p, no_projects, all_possible_v):
    phi = p/(1-p)
    mu_p = get_mu_p(u, phi, no_projects, all_possible_v)
    dist = d_swap(v, u, no_projects)
    # print('d_swap: ', dist)
    # print('1/mu_p: ', 1/mu_p)
    # print('phi: ', phi)
    return 1/mu_p * phi ** (-dist)


if __name__ == '__main__':
    random.seed(datetime.now())
    no_projects = 3
    p = 0.6
    phi = p/(1-p)
