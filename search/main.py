"""
COMP30024 Artificial Intelligence, Semester 1, 2022
Project Part A: Searching
Authored by: Ying Shan Saw & Jo Eann Chong
Date Authored: 31/03/2022

This script contains the entry point to the program (the code in
`__main__.py` calls `main()`). Your solution starts here!
"""
import sys
import json
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
    # creating board object with json file input
    board = Board(data)

    # finding and processing path with function
    pathfinding(board)

    # closing file
    file.close()
