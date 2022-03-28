from asyncio.windows_events import NULL
from fileinput import close
import heapq
import sys
import json
from types import new_class
from typing import Dict, Tuple, List
from util import valid_adjacent_nodes
from typing import TypeVar, Generic

# If you want to separate your code into separate files, put them
# inside the `search` directory (like this one and `util.py`) and
# then import from them like this:
from util import print_board, print_coordinate, heuristic, generated_adj_nodes,  find_print_path


T = TypeVar('T')
class PriorityQueue(Generic[T]):

    #initialises the contents of the queue
    def __init__(self, elements):
        self.elements: List[Tuple[float, T]] = []
    
    #checks if the queue is empty
    def empty(self) -> bool:
        return len(self) > 0
    
    #puts items into the queue based on its priority
    def put(self, item: T, priority: float):
        heapq.heappush(self.elements, (priority, item))
    
    #pops the item nearest to the goal that is unvisited
    def get(self) ->  T:
        return heapq.heappop(self.elements)[1]

def main_new():
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

def pathfinding(start: tuple, goal: tuple, blocks: list(list()), size: int):
    ###################################INITIALISING DATA########################################
    
    frontier = PriorityQueue()
    frontier.put(start, 0)
    # stores the previous location of a given location tuple
    came_from = dict()
    # stores the cost of a given location
    cost_so_far: Dict[tuple(), int] = dict()
    #initialising values for the starting node
    came_from[start] = NULL
    cost_so_far[start] = 0
    ############################################################################################
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        neighbours = valid_adjacent_nodes(current, size, blocks)
        for next in neighbours:
            new_cost = cost_so_far[current] + heuristic(current, next)
            # if the next node found is has no cost, or the new_cost is less than the current cost
            # record the new (lower) cost into the dictionary
            if next not in cost_so_far.keys() or new_cost < cost_so_far[next]:
                cost_so_far[next] = cost_so_far[current] + 1
                priority = new_cost + heuristic(next, goal)
                
                frontier.put(next, priority)
                came_from[next] = current

    if (frontier.empty()) and (goal not in came_from.keys()):
        print("goal not found")
        return NULL
    else:
        find_print_path(start, goal, came_from)

