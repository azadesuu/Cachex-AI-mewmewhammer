"""
COMP30024 Artificial Intelligence, Semester 1, 2022
Project Part A: Searching
Authored by: Ying Shan Saw & Jo Eann Chong

This script contains the entry point to the program (the code in
`__main__.py` calls `main()`). Your solution starts here!
"""

import sys
import json

# If you want to separate your code into separate files, put them
# inside the `search` directory (like this one and `util.py`) and
# then import from them like this:
from util import print_board, print_coordinate, heuristic, generated_adj_nodes, min_distance_node

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
    close_nodes = [] # need to add blue nodes
    goal_path = [] 

    open_nodes.append(node_start)
    while len(open_nodes) > 0:

        closest_node, new_open_nodes = min_distance_node(open_nodes.pop(), node_goal, board_size)
        print(closest_node)
        
        if (closest_node == node_goal): 
            goal_path.append(closest_node)
            break
        for node in new_open_nodes:
            if node not in open_nodes:
                open_nodes.append(node)

        close_nodes.append(closest_node)
        goal_path.append(closest_node)


    print(len(goal_path) + "\n")
    for coor in goal_path:
        print(f"({coor[0]},{coor[1]})\n")
    #finished
