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
    

    ############################################################################################
    # creating board object with 
    board = Board(data)
    # finding and processing path with function
    pathfinding(board)
    # closing file
    file.close()


