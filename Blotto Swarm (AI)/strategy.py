# pylint: disable=W0105, W0613, C0116

"""
Edit this file! This is the file you will submit.
"""

import random

"""
NOTE: Each soldier's memory in the final runner will be separate from the others.

WARNING: Do not print anything to stdout. It will break the grading script!
"""

""" 
- castles have too many people on them
- clumping
- enemies swarming
- history global
"""


def greedy(ally: list, enemy: list, offset: int) -> int:
    if enemy[3 + offset] < 8:
        return offset
    return random.randint(-1, 1)


def greedy_efficient(ally: list, enemy: list, offset: int) -> int:
    castle_neighbors = [i + offset for i in range(2, 5)]
    castle_allies = sum(ally[i] for i in castle_neighbors)

    if enemy[3 + offset] < 8:
        return offset
    if castle_allies > 8:
        return -offset
    return random.randint(-1, 1)


def greedy_weighted(ally, enemy, offset):
    castle_neighbors = [i + offset for i in range(2, 5)]
    castle_allies = sum(ally[i] for i in castle_neighbors)
    weighting = 0.35

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


def diversity(ally: list, enemy: list, offset: int) -> int:
    if offset == 0:
        if enemy[3] >= ally[3]:
            return 0
        if enemy[3] < ally[3] - 1:
            if enemy[0] - ally[0] >= enemy[6] - ally[6]:
                if random.random() < 0.1:
                    return -1
            else:
                if random.random() < 0.1:
                    return 1
    if offset != 0:
        if enemy[offset + 3] > ally[offset + 3]:
            return offset
        return -offset
    return offset


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


def random_strategy(ally: list, enemy: list, offset: int) -> int:
    return random.choice([-1, 0, 1])


def simple_greedy(ally, enemy, offset):
    return offset


def get_strategies():
    """
    Returns a list of strategies to play against each other.

    In the local tester, all of the strategies will be used as separate players, and the
    pairwise winrate will be calculated for each strategy.

    In the official grader, only the first element of the list will be used as your strategy.
    """
    strategies = [greedy_efficient, greedy_weighted]

    return strategies
