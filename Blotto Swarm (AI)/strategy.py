"""
Edit this file! This is the file you will submit.
"""

import random

"""
NOTE: Each soldier's memory in the final runner will be separate from the others.

WARNING: Do not print anything to stdout. It will break the grading script!
"""

def strategy(ally: list, enemy: list, offset: int) -> int:
    # If we are at a castle
    if offset == 0:
        if ally[3] > 10:
            return random.choice([-1, 1])
    elif offset == -1:
        num_enemies = enemy[2] + enemy [3] + enemy [1]
        if num_enemies > 15:
            return -offset
        return offset
    elif offset == 1:
        num_enemies = enemy[3] + enemy[4] + enemy[5]
        if num_enemies > 15:
            return -offset
        return offset
    # ttest
 
def random_strategy(ally: list, enemy: list, offset: int) -> int:
    # A simple strategy
    return random.choice([-1, 0, 1])


def get_strategies():
    """
    Returns a list of strategies to play against each other.

    In the local tester, all of the strategies will be used as separate players, and the 
    pairwise winrate will be calculated for each strategy.

    In the official grader, only the first element of the list will be used as your strategy.
    """
    strategies = [strategy, random_strategy]

    return strategies
