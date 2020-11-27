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

from utilities.mallows_helper import *
from constants import no_projects, mallows_p
from random import random


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
        return self.permutations[j]
