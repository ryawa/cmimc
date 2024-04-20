"""
Edit this file! This is the file you will submit.
"""

import random
import sys

"""
NOTE: Each soldier's memory in the final runner will be separate from the others.

WARNING: Do not print anything to stdout. It will break the grading script!
"""

def base(ally: list, enemy: list, offset: int) -> int:
    if enemy[3 + offset] < 8:
        return offset
    return random.randint(-1, 1)
    # clumping
    # enemies swarming
 
def new(ally: list, enemy: list, offset: int) -> int:
    castle_neighbors = [i + offset for i in range(2, 5)]
    castle_allies = sum([ally[i] for i in castle_neighbors])
    castle_enemies = sum([enemy[i] for i in castle_neighbors])
    
    if enemy[3 + offset] < 8:
        return offset
    if castle_allies > 8:
        return -offset
    return random.randint(-1, 1)

def new_run(ally, enemy, offset):
    castle_neighbors = [i + offset for i in range(2, 5)]
    castle_allies = sum([ally[i] for i in castle_neighbors])
    castle_enemies = sum([enemy[i] for i in castle_neighbors])
    
    if enemy[3 + offset] < 8:
        return offset
    if castle_allies > 8:
        return -offset
    if castle_enemies > 15:
        return -offset
    return random.randint(-1, 1)
#test
def random_strategy(ally: list, enemy: list, offset: int) -> int:
    return random.choice([-1, 0, 1])


def get_strategies():
    """
    Returns a list of strategies to play against each other.

    In the local tester, all of the strategies will be used as separate players, and the 
    pairwise winrate will be calculated for each strategy.

    In the official grader, only the first element of the list will be used as your strategy.
    """
    strategies = [base, new, new_run]

    return strategies