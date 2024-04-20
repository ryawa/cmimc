"""
Edit this file! This is the file you will submit.
"""

import random
import sys

"""
NOTE: Each soldier's memory in the final runner will be separate from the others.

WARNING: Do not print anything to stdout. It will break the grading script!
"""

def ryan(ally: list, enemy: list, offset: int) -> int:
    if offset == 0 and enemy[3] < 7:
        return 0
    return 1

def roger(ally: list, enemy: list, offset: int) -> int:
    # If we are at a castle
    castle_neighbors = [2, 3, 4]
    castle_neighbors = [x + offset for x in castle_neighbors]
    num_allies = sum([ally[i] for i in castle_neighbors])
    num_enemies = sum([enemy[i] for i in castle_neighbors])
    if offset == 0:
        if ally[3] > 7:
            return random.choice([-1, 1])
    elif offset == -1:
        # print(castle_neighbors, file=sys.stderr)
        if num_enemies > 7:
            return -offset
        return offset
    elif offset == 1:
        if num_enemies > 7:
            return -offset
        return offset
 
def wenhao(ally: list, enemy: list, offset: int) -> int:
    # A simple strategy
    return offset

def get_strategies():
    """
    Returns a list of strategies to play against each other.

    In the local tester, all of the strategies will be used as separate players, and the 
    pairwise winrate will be calculated for each strategy.

    In the official grader, only the first element of the list will be used as your strategy.
    """
    strategies = [wenhao, roger, ryan]

    return strategies