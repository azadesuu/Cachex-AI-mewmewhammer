"""
COMP30024 Artificial Intelligence, Semester 1, 2022
Project Part A: Searching
Authored by: Ying Shan Saw & Jo Eann Chong

This script contains the entry point to the program (the code in
`__main__.py` calls `main()`). Your solution starts here!
"""

from fileinput import close
from heapq import merge
import sys
import json
from types import new_class

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
    blocks = []
    for block_nodes in data["board"]:
        blocks.append(block_nodes[1:3])

    node_start = data["start"]
    node_goal = data["goal"]

    open_nodes = []
    close_nodes = [] # need to add blue nodes
    goal_path = [node_start] 

    open_nodes.append(node_start)
    for b in blocks:
        close_nodes.append(b)

    while len(open_nodes) > 0:
        print("    popped node:" + str(open_nodes[-1]))
        closest_node, new_open_nodes = min_distance_node(open_nodes.pop(), node_goal, board_size, blocks, close_nodes)
        print("cl node: " + str(closest_node))
        
        print("NEW:" + str(new_open_nodes))

        if (closest_node == node_goal): 
            goal_path.append(closest_node)
            break
        
        if closest_node not in close_nodes:
            close_nodes.append(closest_node)
        
        for node in new_open_nodes:
            if (node not in close_nodes) and (node not in open_nodes):
                open_nodes.append(node)

        goal_path.append(closest_node)
        # print("GOAL:" + str(goal_path))
        
        print("cn:"+ str(close_nodes))


        open_nodes.append(closest_node)
        print("on:"+ str(open_nodes))
    

    print(str(len(goal_path)))
    for coor in goal_path:
        print(f"({coor[0]},{coor[1]})")
        
    #finished
