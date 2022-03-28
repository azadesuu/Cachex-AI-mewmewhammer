from asyncio.windows_events import NULL
from fileinput import close
import heapq
import sys
import json
from types import new_class
from typing import Dict, Tuple, List
# from search.util import valid_adjacent_nodes
from typing import TypeVar, Generic

# If you want to separate your code into separate files, put them
# inside the `search` directory (like this one and `util.py`) and
# then import from them like this:
from util import print_board, print_coordinate, heuristic, generated_adj_nodes,  find_print_path, UNIT_COST, valid_adjacent_nodes


T = TypeVar('T')
class PriorityQueue():

    #initialises the contents of the queue
    def __init__(self):
        self.elements: List[Tuple[float, T]] = []
    
    #checks if the queue is empty
    def empty(self) -> bool:
        return not self.elements
    
    #puts items into the queue based on its priority
    def put(self, item: T, priority: float):
        heapq.heappush(self.elements, (priority, item))
    
    #pops the item nearest to the goal that is unvisited
    def get(self) ->  T:
        return heapq.heappop(self.elements)[1]

def main():
    ###################################IMPORTING DATA#########################################
    try:
        with open(sys.argv[1]) as file:
            data = json.load(file)      
    except IndexError:
        print("usage: python3 -m search path/to/input.json", file=sys.stderr)
        sys.exit(1)
    
    # board dimensions
    board_size = data["n"]
    #putting in closed nodes (cannot be visited)
    blocks = []
    for block_nodes in data["board"]:
        blocks.append(block_nodes[1:3])

    node_start = tuple(data["start"])
    node_goal = tuple(data["goal"])
    ############################################################################################
    pathfinding(node_start, node_goal, blocks, board_size)

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
        cost_so_far[tuple(block)]  = 0

    found = False
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            found = True
            break
        neighbours = valid_adjacent_nodes(current, size, blocks)
        for next_node in neighbours:
            t_next_node = tuple(next_node)

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

