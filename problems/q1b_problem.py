import logging
import time
from typing import Tuple

import util
from game import Actions, Agent, Directions
from logs.search_logger import log_function
from pacman import GameState


class q1b_problem:
    """
    This search problem finds paths through all four corners of a layout.

    You must select a suitable state space and successor function
    """
    def __str__(self):
        return str(self.__class__.__module__)

    def __init__(self, gameState: GameState):
        """
        Stores the start and goal.

        gameState: A GameState object (pacman.py)
        costFn: A function from a search state (tuple) to a non-negative number
        goal: A position in the gameState
        """
        self.startingGameState: GameState = gameState

    @log_function
    def getStartState(self):
        "*** YOUR CODE HERE ***"
        return self.startingGameState

    @log_function
    def isGoalState(self, state):
        "*** YOUR CODE HERE ***"
        return state ==0

    @log_function
    def getSuccessors(self, state):
        """
        Returns successor states, the actions they require, and a cost of 1.

         As noted in search.py:
             For a given state, this should return a list of triples,
         (successor, action, stepCost), where 'successor' is a
         successor to the current state, 'action' is the action
         required to get there, and 'stepCost' is the incremental
         cost of expanding to that successor
        """
        "*** YOUR CODE HERE ***"
        #Retrieve set of legal actions pacman can take:
        action_lst = state.getLegalPacmanActions()

        states = []
        pacman_positions = []

        #Cost of every action is 1
        cost = 1

        for action in action_lst:
            
            #Retrieve the the successor state after the specified pacman action
            successor_state = state.generatePacmanSuccessor(action)

            #Retrieve the pacman position in the successor state (after the action):
            success_pos = successor_state.getPacmanPosition()

            states.append(successor_state)
            pacman_positions.append(success_pos)

        
        return states,action_lst,pacman_positions,cost


