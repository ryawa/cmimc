# pylint: disable=W0105, W0603, W0613, C0103, C0116

"""
Edit this file! This is the file you will submit.
"""

import random

"""
NOTE: Each soldier's memory in the final runner will be separate from the others.

WARNING: Do not print anything to stdout. It will break the grading script!
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


def base(ally, enemy, offset):
    max_lead = 3
    min_loss = -5
    castle_lead = ally[3 + offset] - enemy[3 + offset]
    if offset == 0:
        if castle_lead >= max_lead:
            if random.random() < (1 / ally[3]):
                return random.randint(-1, 1)
        if castle_lead <= min_loss:
            return random.randint(-1, 1)
        return 0
    far_castle = 3 - 2 * offset
    far_castle_lead = ally[far_castle] - enemy[far_castle]
    if far_castle_lead < castle_lead or castle_lead >= max_lead:
        return -offset
    return offset


'''
-when bait = false:
    do what we normally do: base()
-when enemy has more than 6 and we are currently losing by 2? Bait =true
'''
bait = False 
bait_direction = 0 #direction soldiers run away to
steps_taken = 0 #num of steps taken away from castle
steps_taken_back = 0 #num of steps going back
going_back = False #done baiting and going back
def bait_soldiers(ally, enemy, offset):
    global bait, bait_direction, steps_taken, steps_taken_back, going_back
    if offset == 0 and enemy[3] > 6 and enemy[3] - ally[3] >= 2:
        bait = True
    if bait == False:
        max_lead = 3
        min_loss = -5
        castle_lead = ally[3 + offset] - enemy[3 + offset]
        if offset == 0:
            if castle_lead >= max_lead:
                if random.random() < (1 / ally[3]):
                    return random.randint(-1, 1) # we should go to castle that needs more help instead of random
            if castle_lead <= min_loss:
                return random.randint(-1, 1)
            return 0
        far_castle = 3 - 2 * offset
        far_castle_lead = ally[far_castle] - enemy[far_castle]
        if far_castle_lead < castle_lead or castle_lead >= max_lead:
            return -offset
        return offset
    else:
        # first check if done baiting
        if steps_taken_back == 3:
            bait = False # reset everything
            bait_direction = 0
            steps_taken = 0
            steps_taken_back = 0
            going_back = False

        #check which castle to go towards
        if offset == 0 and steps_taken == 0: #if soldier is currently on the castle and hasnt taken any steps away
            if enemy[0] - ally[0] > enemy[6] - ally[6]:
                bait_direction = -1
            else:
                bait_direction = 1
        
        if steps_taken != 3:
            steps_taken +=1
            return bait_direction
        else:
            if bait_direction == -1 and enemy[6] <3:
                going_back = True
            if bait_direction == 1 and enemy[0] < 3:
                going_back = True

            if going_back == True:
                steps_taken_back += 1
                return -bait_direction
            return 0 #if not going back, stay
        
        


def get_strategies():
    """
    Returns a list of strategies to play against each other.

    In the local tester, all of the strategies will be used as separate players, and the
    pairwise winrate will be calculated for each strategy.

    In the official grader, only the first element of the list will be used as your strategy.
    """
    strategies = [base, simple_greedy, bait_soldiers]

    return strategies
