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
    random.seed(10)
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

def new_weighting4(ally, enemy, offset): # adds a weighting to the random decisons in new(). Currently highest scoring one 
    castle_neighbors = [i + offset for i in range(2, 5)]
    castle_allies = sum([ally[i] for i in castle_neighbors])
    castle_enemies = sum([enemy[i] for i in castle_neighbors])
    weighting = 0.4 #based off of testing, optimal weighting is 0.3 or 0.4
    
    if enemy[3 + offset] < 8:
        return offset
    if castle_allies > 8:
        return -offset
    if offset == -1:
        if random.random() < weighting:
            return -1
        else:
            return 1
    if random.random() < weighting:
        return 1
    return -1

def diversity(ally: list, enemy: list, offset: int) -> int:
# different method. Basically uses if else statments to determine whether to stay or leave. Offers diversity for testing purposes
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
        if enemy[offset+3] > ally[offset+3]:
            return offset
        else:
            return -offset     
    return offset

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
def return_offset(ally, enemy, offset):
    return offset


def get_strategies():
    """
    Returns a list of strategies to play against each other.

    In the local tester, all of the strategies will be used as separate players, and the 
    pairwise winrate will be calculated for each strategy.

    In the official grader, only the first element of the list will be used as your strategy.
    """
    strategies = [new, new_weighting4]

    return strategies