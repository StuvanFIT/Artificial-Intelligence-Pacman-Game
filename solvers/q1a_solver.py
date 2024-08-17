#---------------------#
# DO NOT MODIFY BEGIN #
#---------------------#

import logging
import util

from problems.q1a_problem import q1a_problem

def q1a_solver(problem: q1a_problem):
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

        #This is the open set: the states/nodes to be explored
        self.open_set = util.PriorityQueue()

        #This is our visited set: nodes already explored
        self.closed_set = []

        self.g_val_table = {} # g(n) values at each state
        
        self.f_val_table = {} # f(n) = g(n) + h(n)

        self.parent_table = {} #This is basically the list that reconstructs our path to the goal

        self.goal_pos = (0,0)


def astar_initialise(problem: q1a_problem):
    # YOUR CODE HERE
    #NOT COMPULSORY FUNCTION

    #Initialisation Stage of the A* algorithm
    #We need to intialise the starting values and positions
    astarData = AStarData()

    #Retrieve the start state:
    start_state = problem.getStartState()
    start_position = start_state.getPacmanPosition() #- Return an (x,y) tuple with the location of Pac-Man on the grid

    #Find position of the food (our goal) on this grid map
    locations_of_food = start_state.getFood()
    goal_position = (0,0)

    for x in range(locations_of_food.width):
        for y in range(locations_of_food.height):

            if locations_of_food[x][y] == True:
                goal_position = (x,y)
    
    astarData.goal_pos = goal_position


    #initialise the g and f values:
    astarData.g_val_table[start_position] = 0 #distance is 0 at start
    intial_h_value = astar_heuristic(start_position, goal_position)

    astarData.f_val_table[start_position] = intial_h_value

    #Append start position:
    #The data structure representation 
    """
    (current_position, current_state)
    Priority is based on the f-value, minimum f value
    """
    astarData.open_set.push((start_position, start_state), astarData.f_val_table[start_position] )



    return astarData



def astar_loop_body(problem: q1a_problem, astarData: AStarData):
    # YOUR CODE HERE


    if astarData.open_set.isEmpty():
        return "NO SOLUTION HAS BEEN FOUND:Open Set is empty and no more nodes to expand"
    

    #Note: no while loop, loop body is just the "action bit"
    #Pop the node off the open set:
    current_position, current_state = astarData.open_set.pop()

    #If we have found the goal node (the number of food on the game grid is 0), then we need to reconstruct the path:
    if problem.isGoalState(current_state):
        pathway = reconstruct_path(astarData, current_position)
        return True, pathway
    
    #ADD IT TO THE CLOSED SET TO AVOID POTENIALLY REEXPANDING:
    #Need to add before loop and not at the end, as we want to check in the expansion.
    astarData.closed_set.append(current_position)


    
    #If we havent found the goal node, we need to expand the successor or neighbouring nodes:
    for successor_state, required_action, cost in problem.getSuccessors(current_state):

        #Find the coorindates of the pac man in the successor state
        successor_position = successor_state.getPacmanPosition()

        if check_already_expanded(astarData, successor_position):

            #Current g-value:
            curr_g_val = astarData.g_val_table[current_position]
            #Calculate new g-value
            new_g_val = curr_g_val + cost



            #So if the new g(n) value is lower, then we need to update the g value
            if  successor_position not in astarData.g_val_table or new_g_val < astarData.g_val_table[successor_position]:

                #Update the parent node: we need the action to get reconstruct the path at the end
                astarData.parent_table[successor_position] = (required_action, current_position)

                #update the new g value at the node since it is lower or better:
                astarData.g_val_table[successor_position] = new_g_val

                astarData.f_val_table[successor_position] = new_g_val + astar_heuristic(successor_position, astarData.goal_pos)

                #Finally, we add it to the open set
                astarData.open_set.push((successor_position, successor_state), astarData.f_val_table[successor_position])


    return (False,None)

def check_already_expanded(astarData, current_node):

    return current_node not in astarData.closed_set


def reconstruct_path(astarData, current_position):
    
    optimal_route =[]

    while current_position in astarData.parent_table:

        required_action, current_position = astarData.parent_table[current_position]

        optimal_route.append(required_action)
    
    optimal_route.reverse()

    return optimal_route


        
def astar_heuristic(current, goal):
    # YOUR CODE HERE

    #Manhattan heuristic function:
    #Since the goal is a single piece of food, then we just calcualte the manhattan distance between current 
    #position and the food
    return util.manhattanDistance(current, goal)


    


    



   


