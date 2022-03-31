import sys
import json
# from search.util import valid_adjacent_nodes
# If you want to separate your code into separate files, put them
# inside the `search` directory (like this one and `util.py`) and
# then import from them like this:
from util import pathfinding
from classes import Board

def main():
    ###################################IMPORTING DATA#########################################
    try:
        with open(sys.argv[1]) as file:
            data = json.load(file)      
    except IndexError:
        print("usage: python3 -m search path/to/input.json", file=sys.stderr)
        sys.exit(1)
    

    ############################################################################################
    # creating board object with 
    board = Board(data)
    # finding and processing path with function
    pathfinding(board)
    # closing file
    file.close()

def pathfinding(start: tuple, goal: tuple, blocks: List[List], size: int):
    ###################################INITIALISING DATA########################################
    frontier = PriorityQueue()
    frontier.put(start, 0)
    # stores the previous location of a given location tuple
    came_from = dict()
    # stores the cost of a given location
    cost_so_far: Dict[Tuple, int] = dict()
    #initialising values for the starting nodes
    came_from[start] = NULL
    cost_so_far[start] = 0
    ############################################################################################
    #initialising blocks
    for block in blocks:
        came_from[tuple(block)] = NULL
        cost_so_far[tuple(block)] = 0

    found = False
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            found = True
            break
        neighbours = valid_adjacent_nodes(current, size, blocks)
        for next_node in neighbours:
            t_next_node = tuple(next_node)
            print(t_next_node)
            #cost of next node to goal
            new_cost = UNIT_COST + heuristic(t_next_node, goal)
            # if the next node found is has no cost, or the new_cost is less than the current cost
            # record the new (lower) cost into the dictionary
            if t_next_node not in cost_so_far.keys() or new_cost < cost_so_far[t_next_node]:
                cost_so_far[t_next_node] = new_cost
                priority = new_cost
                
                frontier.put(t_next_node, priority)
                came_from[t_next_node] = current

    if ((frontier.empty()) and (goal not in came_from.keys())) or (not found):
        print("goal not found")
        exit(-1)    
    else:
        find_print_path(start, goal, came_from)
