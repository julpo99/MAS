import itertools
from math import comb


def shapley_value(player):
    N = {1, 2, 3, 4, 5}
    N.remove(player)

    subsets = []

    for i in range(5):
        subsets.extend(findsubsets(N, i))

    sum = 0
    for subset in subsets:
        sum += marginal_contribution(set(subset), player) * (1/comb(4, len(subset)))

    sum /= 5 # divide by n

    return sum

def marginal_contribution(S, i):
    S_i = S.union(set([i]))
    return value(S_i) - value(S)


def value(S):
    if (1 in S and len(S) >= 2) or set([2, 3, 4, 5]) <= set(S):
        return 1
    else:
        return 0


def findsubsets(s, n):
    return list(itertools.combinations(s, n))


for i in range(1, 6):
    print(f"For player {i}: {shapley_value(i)}")