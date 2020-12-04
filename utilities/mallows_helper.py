# Generates all possible rankings for a given number of projects.
import itertools
from random import randint
from constants import min_utility, max_utility, division


# # Returns the combination (nCr): the number of ways in which r elements can be chosen from n objects.
# def ncr(n, r):
#     r = min(r, n-r)
#     numer = reduce(op.mul, range(n, n-r, -1), 1)
#     denom = reduce(op.mul, range(1, r+1), 1)
#     return numer // denom


# TODO really slow for a large number of voters (and unnecessary because of law of large numbers).
from utilities.mallows import Mallows


def spread_voters(no_u, no_voters):
    if no_u == 1:
        return [no_voters]
    else:
        l = [division * no_voters]
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
        flip[i] = ranking[-(i+1)]
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

