#---------------------#
# DO NOT MODIFY BEGIN #
#---------------------#

import logging

import util
from problems.q1b_problem import q1b_problem

def q1b_solver(problem: q1b_problem):
    astarData = astar_initialise(problem)
    num_expansions = 0
    terminate = False
    while not terminate:
        num_expansions += 1
        terminate, result = astar_loop_body(problem, astarData)
    print(f'Number of node expansions: {num_expansions}')
    return result

#-------------------#
# DO NOT MODIFY END #
#-------------------#

class AStarData:
    # YOUR CODE HERE
    def __init__(self):
        pass

def astar_initialise(problem: q1b_problem):
    # YOUR CODE HERE
    astarData = AStarData()
    astarData.x = 'stuff'
    astarData.y = 123
    return astarData

def astar_loop_body(problem: q1b_problem, astarData: AStarData):
    # YOUR CODE HERE
    util.raiseNotDefined()  # Delete this line

def astar_heuristic(current, goals):
    # YOUR CODE HERE
    return 0
