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
import itertools

from constants import *
from random import random, randint


class Mallows:

    def __init__(self, u, permutations):
        self.u = u
        self.permutations = permutations

        self.phi = mallows_p / (1 - mallows_p)
        self.mu_p = self.get_mu_p(u)

        self.probabilities = len(permutations) * [0]
        for i, v in enumerate(permutations):
            self.probabilities[i] = self._probability(v)

    # Returns mu_p, where mu_p is the sum over all possible rankings v given a set of projects
    # of phi ** (- d_swap(v,u))
    def get_mu_p(self, u):
        sum_mu = 0
        for v in self.permutations:
            sum_mu += self.phi ** (-d_swap(v, u, no_projects))
        return sum_mu

    def _probability(self, v):
        dist = d_swap(v, self.u, no_projects)
        return 1 / self.mu_p * self.phi ** (-dist)

    # Select a random ranking permutations[j], taking into account the probabilities of each ranking.
    def draw_ranking(self):
        num = random()
        sum_p = self.probabilities[0]
        j = 0
        while num > sum_p:
            sum_p += self.probabilities[j]
            j += 1
        if j >= len(self.permutations):
            return self.permutations[j-1]
        return self.permutations[j]


# # Returns the combination (nCr): the number of ways in which r elements can be chosen from n objects.
# def ncr(n, r):
#     r = min(r, n-r)
#     numer = reduce(op.mul, range(n, n-r, -1), 1)
#     denom = reduce(op.mul, range(1, r+1), 1)
#     return numer // denom

def spread_voters(no_u, no_voters):
    if no_u == 1:
        return [no_voters]
    else:
        l = [int(division * no_voters)]
        l.append(no_voters - l[0])
        return l


def all_possible_rankings(no_projects):
    basis = list(range(no_projects))
    return list(itertools.permutations(basis))


def pick_random(permutations):
    return permutations[randint(0, len(permutations) - 1)]


# Returns the swap distance: the number of elements one should swap in one ranking to obtain
# the other. Formally, the number of pairs (c, c′) ∈ A × A such that u ranks c above c′, but v
# ranks c′ above c.
# Can also be calculated with: nCr(no_projects, 2) - k, where k is the number of rankings u and v
# agree on.
# FIXME
def d_swap(v, u, no_projects):
    count = 0
    for i in range(no_projects - 1):
        for j in range(i + 1, no_projects):
            if (v.index(i) > v.index(j)) != (u.index(i) > u.index(j)):
                # u and v do not agree on the ranking of alternatives i and j.
                count += 1
    return count


def flip(ranking):
    flip = [0] * len(ranking)
    for i in range(len(ranking)):
        flip[i] = ranking[-(i + 1)]
    return flip


# Helper function of utilities_mallows.
# Generates a dictionary of utilities per voter for every project using Mallows' model.
def true_ranking_utilities(u, permutations, no_voters_u, start_no):
    model = Mallows(u, permutations)

    # Generate voters' utilities for projects, based on the probabilities of rankings.
    utilities = {}
    for index in range(no_voters_u):
        ranking = model.draw_ranking()

        # Generate utilities and order based on permutations[j].
        random_utilities = [randint(min_utility, max_utility) for _ in range(no_projects)]
        random_utilities.sort(reverse=True)
        random_utilities = [(random_utilities[index], index) for index in range(no_projects)]
        random_utilities.sort(key=(lambda x: ranking[x[1]]))

        # Add result to dictionary 'utilities'.
        name = 'voter' + str(start_no + index)
        utilities[name] = [random_utilities[idx][0] for idx in range(no_projects)]
    return utilities
