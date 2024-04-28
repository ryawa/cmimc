# pylint: disable=W0105, W0603, W0613, C0103, C0116

"""
Edit this file! This is the file you will submit.
"""

import random

"""
NOTE: Each soldier's memory in the final runner will be separate from the others.

WARNING: Do not print anything to stdout. It will break the grading script!
"""


def greedy_weighted(ally, enemy, offset):
    castle_neighbors = [i + offset for i in range(2, 5)]
    castle_allies = sum(ally[i] for i in castle_neighbors)
    weighting = 0.4

    if enemy[3 + offset] < 8:
        return offset
    if castle_allies > 8:
        return -offset
    if offset == -1:
        if random.random() < weighting:
            return -1
        return 1
    if random.random() < weighting:
        return 1
    return -1


def greedy_run(ally, enemy, offset):
    castle_neighbors = [i + offset for i in range(2, 5)]
    castle_allies = sum(ally[i] for i in castle_neighbors)
    castle_enemies = sum(enemy[i] for i in castle_neighbors)

    if enemy[3 + offset] < 8:
        return offset
    if castle_allies > 8:
        return -offset
    if castle_enemies > 15:
        return -offset
    return random.randint(-1, 1)


def offset(ally, enemy, offset):
    return offset


# dont get baited
# periodically leave
# leave if losing and no one nearby
# leave after 25 days?
def base(ally, enemy, offset):
    max_lead = 3
    min_loss = -5
    castle_lead = ally[3 + offset] - enemy[3 + offset]
    if offset == 0:
        if enemy[0] - ally[0] > enemy[6] - ally[6]:
            losing_offset = -1
        else:
            losing_offset = 1
        if castle_lead >= max_lead or castle_lead < 0:
            if random.random() < (1 / ally[3]):
                return losing_offset
        if castle_lead <= min_loss:
            return losing_offset
        return 0
    far_castle = 3 - 2 * offset
    far_castle_lead = ally[far_castle] - enemy[far_castle]
    if castle_lead <= 0 < castle_lead + ally[3]:
        return offset
    if far_castle_lead <= 0 < far_castle_lead + ally[3]:
        return -offset
    if far_castle_lead < castle_lead or castle_lead >= max_lead:
        return -offset
    return offset


def get_strategies():
    """
    Returns a list of strategies to play against each other.

    In the local tester, all of the strategies will be used as separate players, and the
    pairwise winrate will be calculated for each strategy.

    In the official grader, only the first element of the list will be used as your strategy.
    """
    strategies = [base, offset]

    return strategies
