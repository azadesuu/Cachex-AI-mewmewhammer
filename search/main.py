from asyncio.windows_events import NULL
from fileinput import close
import sys
import json
from types import new_class
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
    
    board = Board(data)
    # board dimensions
    board_size = getattr(board, 'size')
    blocks = getattr(board, 'blocks')
    node_start = tuple(getattr(board, 'blocks'))
    node_goal = tuple(getattr(board, 'goal'))

    ############################################################################################
    pathfinding(node_start, node_goal, blocks, board_size)
    file.close()


