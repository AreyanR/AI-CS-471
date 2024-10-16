# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
     # create a stack 
    stack = util.Stack()
     # push the start state and an empty list to the stack 
     # path list will keep track o factions taken to reach each state
    stack.push((problem.getStartState(), []))

    #create a set to keep track of explored states
    explored = set() 

    #while the stack is not empty
    while not stack.isEmpty():
        
        #pop the state and path from the stack
        state, path = stack.pop()

        #check if that state is a goal state , if so return the path to it
        if problem.isGoalState(state):
            return path
        
        # if the state has not been explored
        if state not in explored:

            #mark it as explored 
            explored.add(state)

            #expand the current state by checking each of its succesors             find succsor fucntions
            for successor, action, cost in problem.getSuccessors(state):
                # if successor has not been exploredm add it to the stack
                if successor not in explored:
                    #update path by adding the action taken to reach this sucessor
                    stack.push((successor, path + [action]))
                    
    #if no paths are found return an empty list
    return []
    
    

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    
    # Push the start state onto the queue along with an empty path
    queue.push((problem.getStartState(), []))
    
    # Use a set to track explored states
    explored = set()
    
    while not queue.isEmpty():
        # Pop the next node (FIFO order for BFS)
        state, path = queue.pop()
        
        # Goal test
        if problem.isGoalState(state):
            return path
        
        # Mark the current state as explored
        if state not in explored:
            explored.add(state)
            
            # Expand the node by exploring its successors
            for successor, action, cost in problem.getSuccessors(state):
                if successor not in explored and not any(successor == s for s, _ in queue.list):
                    # Push successor onto the queue with updated path
                    queue.push((successor, path + [action]))
                    
    return []


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    priority_queue = util.PriorityQueue()
    
    # Push the start state with an initial cost of 0
    # The path list will store the sequence of actions taken to reach this state
    priority_queue.push((problem.getStartState(), [], 0), 0)  # (state, path, cost), priority = cost
    
    # Use a dictionary to track the lowest cost at which each state has been explored
    explored = {}

    # While there are nodes to explore in the priority queue
    while not priority_queue.isEmpty():
        # Pop the node with the lowest cumulative cost
        state, path, cost = priority_queue.pop()

        # Check if the current state is the goal state; if so, return the path to it
        if problem.isGoalState(state):
            return path
        
        # If the state hasn't been explored at a lower cost
        if state not in explored or cost < explored[state]:
            # Mark the state as explored with this cost
            explored[state] = cost
            
            # Expand the current state by checking each of its successors
            for successor, action, step_cost in problem.getSuccessors(state):
                # Calculate the cumulative cost to reach this successor
                new_cost = cost + step_cost
                # If the successor hasn't been explored at a lower cost
                if successor not in explored or new_cost < explored.get(successor, float('inf')):
                    # Push the successor onto the priority queue with the updated cost and path
                    priority_queue.push((successor, path + [action], new_cost), new_cost)

    # If no solution is found, return an empty list
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

