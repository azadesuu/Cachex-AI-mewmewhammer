"""
COMP30024 Artificial Intelligence, Semester 1, 2022
Project Part A: Searching

This script contains the entry point to the program (the code in
`__main__.py` calls `main()`). Your solution starts here!
"""

import sys
import json

# If you want to separate your code into separate files, put them
# inside the `search` directory (like this one and `util.py`) and
# then import from them like this:
from util import print_board, print_coordinate, heuristic, valid_adjacent_moves, generated_adj_nodes
UNITCOST = 1

def main():
    try:
        with open(sys.argv[1]) as file:
            data = json.load(file)      
    except IndexError:
        print("usage: python3 -m search path/to/input.json", file=sys.stderr)
        sys.exit(1)
        
    # TODO:
    # Find and print a solution to the board configuration described
    # by `data`.
    # Why not start by trying to print this configuration out using the
    # `print_board` helper function? (See the `util.py` source code for
    # usage information).

    board_size = data["n"]
    blocks = data["board"]
    node_start = data["start"]
    node_goal = data["goal"]

    open_nodes = []
    close_nodes = []

    open_nodes.append(node_start)
    while not open_nodes.empty():
        for node in valid_adjacent_moves(open_nodes.pop(), board_size):
            goal_distance = UNITCOST + heuristic(node, node_goal)
            # if goal_distance == UNITCOST:
                # add node to path
        

