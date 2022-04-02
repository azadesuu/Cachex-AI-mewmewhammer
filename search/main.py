import sys
import json
# If you want to separate your code into separate files, put them
# inside the `search` directory (like this one and `util.py`) and
# then import from them like this:

"""
COMP30024 Artificial Intelligence, Semester 1, 2022
Project Part A: Searching
Authored by: Ying Shan Saw & Jo Eann Chong
Date Authored: 31/03/2022

This script contains the entry point to the program (the code in
`__main__.py` calls `main()`). Your solution starts here!
"""

from util import pathfinding,print_board
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
    print_board(board.size, board.board)

    # closing file
    file.close()
