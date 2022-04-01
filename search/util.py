"""
COMP30024 Artificial Intelligence, Semester 1, 2022
Project Part A: Searching

This module contains some helper functions for printing actions and boards.
Feel free to use and/or modify them to help you develop your program.
"""

from itertools import islice

import math
from classes import PriorityQueue, Board, Nodes
from typing import List, Dict, Tuple
UNIT_COST = 1

def apply_ansi(str, bold=True, color=None):
    """
    Wraps a string with ANSI control codes to enable basic terminal-based
    formatting on that string. Note: Not all terminals will be compatible!
    Don't worry if you don't know what this means - this is completely
    optional to use, and not required to complete the project!

    Arguments:

    str -- String to apply ANSI control codes to
    bold -- True if you want the text to be rendered bold
    color -- Colour of the text. Currently only red/"r" and blue/"b" are
        supported, but this can easily be extended if desired...

    """
    bold_code = "\033[1m" if bold else ""
    color_code = ""
    if color == "r":
        color_code = "\033[31m"
    if color == "b":
        color_code = "\033[34m"
    return f"{bold_code}{color_code}{str}\033[0m"

def print_coordinate(r, q, **kwargs):
    """
    Output an axial coordinate (r, q) according to the format instructions.

    Any keyword arguments are passed through to the print function.
    """
    print(f"({r},{q})", **kwargs)

def print_board(n, board_dict, message="", ansi=False, **kwargs):
    """
    For help with visualisation and debugging: output a board diagram with
    any information you like (tokens, heuristic values, distances, etc.).

    Arguments:

    n -- The size of the board
    board_dict -- A dictionary with (r, q) tuples as keys (following axial
        coordinate system from specification) and printable objects (e.g.
        strings, numbers) as values.
        This function will arrange these printable values on a hex grid
        and output the result.
        Note: At most the first 5 characters will be printed from the string
        representation of each value.
    message -- A printable object (e.g. string, number) that will be placed
        above the board in the visualisation. Default is "" (no message).
    ansi -- True if you want to use ANSI control codes to enrich the output.
        Compatible with terminals supporting ANSI control codes. Default
        False.
    
    Any other keyword arguments are passed through to the print function.

    Example:

        >>> board_dict = {
        ...     (0, 4): "hello",
        ...     (1, 1): "r",
        ...     (1, 2): "b",
        ...     (3, 2): "$",
        ...     (2, 3): "***",
        ... }
        >>> print_board(5, board_dict, "message goes here", ansi=False)
        # message goes here
        #              .-'-._.-'-._.-'-._.-'-._.-'-.
        #             |     |     |     |     |     |
        #           .-'-._.-'-._.-'-._.-'-._.-'-._.-'
        #          |     |     |  $  |     |     |
        #        .-'-._.-'-._.-'-._.-'-._.-'-._.-'
        #       |     |     |     | *** |     |
        #     .-'-._.-'-._.-'-._.-'-._.-'-._.-'
        #    |     |  r  |  b  |     |     |
        #  .-'-._.-'-._.-'-._.-'-._.-'-._.-'
        # |     |     |     |     |hello| 
        # '-._.-'-._.-'-._.-'-._.-'-._.-'
        
    """

    stitch_pattern = ".-'-._"
    edge_col_len = 3
    v_divider = "|"
    h_spacing = len(stitch_pattern)
    output = message + "\n"

    # Helper function to only selectively apply ansi formatting if enabled
    apply_ansi_s = apply_ansi if ansi else lambda str, **_: str

    # Generator to repeat pattern string (char by char) infinitely
    def repeat(pattern):
        while True:
            for c in pattern:
                yield c

    # Generate stitching pattern given some offset and length
    def stitching(offset, length):
        return "".join(islice(repeat(stitch_pattern), offset, length))

    # Loop through each row i from top (print ordering)
    # Note that n - i - 1 is equivalent to r in axial coordinates
    for i in range(n):
        x_padding = (n - i - 1) * int(h_spacing / 2)
        stitch_length = (n * h_spacing) - 1 + \
            (int(h_spacing / 2) + 1 if i > 0 else 0)
        mid_stitching = stitching(0, stitch_length)

        # Handle coloured borders for ansi outputs
        # Fairly ugly code, but there is no "simple" solution
        if i == 0:
            mid_stitching = apply_ansi_s(mid_stitching, color="r")
        else:
            mid_stitching = \
                apply_ansi_s(mid_stitching[:edge_col_len], color="b") + \
                mid_stitching[edge_col_len:-edge_col_len] + \
                apply_ansi_s(mid_stitching[-edge_col_len:], color="b")

        output += " " * (x_padding + 1) + mid_stitching + "\n"
        output += " " * x_padding + apply_ansi_s(v_divider, color="b")

        # Loop through each column j from left to right
        # Note that j is equivalent to q in axial coordinates
        for j in range(n):
            coord = (n - i - 1, j)
            value = str(board_dict.get(coord, ""))
            contents = value.center(h_spacing - 1)
            if ansi:
                contents = apply_ansi_s(contents, color=value)
            output += contents + (v_divider if j < n - 1 else "")
        output += apply_ansi_s(v_divider, color="b")
        output += "\n"
    
    # Final/lower stitching (note use of offset here)
    stitch_length = (n * h_spacing) + int(h_spacing / 2)
    lower_stitching = stitching(int(h_spacing / 2) - 1, stitch_length)
    output += apply_ansi_s(lower_stitching, color="r") + "\n"

    # Print to terminal (with optional args forwarded)
    print(output, **kwargs)

# heuristics, the cost of from the current node to goal
def distance_to_goal(current, goal):
    x = ((current[0] - goal[0])**2)
    y = ((current[1] - goal[1])**2)
    distance = abs(math.sqrt(x+y))

    return distance

#checks for nodes adjacent to the current node, and returns the valid ones
def valid_adjacent_nodes(current:tuple, board: Board):
    # generating all adjacent nodes
    adj_nodes = generated_adj_nodes(current)
    # stores only valid adjacent nodes
    valid_adj_nodes = []
    for node in adj_nodes:
        if node not in board.blocks:
            x, y = node[0], node[1]
            # checking if the numbers are within bounds
            if not ((x >= board.size) or (y >= board.size) or (x < 0) or (y < 0)):
                valid_adj_nodes.append(tuple([x, y])) # converting to tuple to use as dictionary key
    return valid_adj_nodes


# generates a list of all adjacent nodes
def generated_adj_nodes(current: tuple):
    # list to store the adjacent nodes, and the one to be returned
    adj_nodes = []
    for y in [-1, 0, 1]:
        for x in [-1, 0, 1]:
            if y == x:
                # the adjacent nodes do not include the nodes where x,y+=0, x,y-=1, x,y+=1
                continue
            else:
                node = []
                node.append(current[0]+x)
                node.append(current[1]+y)
                adj_nodes.append(tuple(node)) # converting to tuple to use as dictionary key
    return adj_nodes


def pathfinding(board: Board):
    # orders the valid adjacent nodes by priority
    priority_queue = PriorityQueue()
    ###################################INITIALISING DATA########################################
    size = board.size
    blocks = board.blocks
    start = board.start
    goal = board.goal
    
    # entering the first node
    priority_queue.put(start, 0)     
    #initialising values for the starting nodes
    board.nodes.came_from[start] = None
    board.nodes.cost_so_far[start] = 0
    #initialising blocks
    for block in blocks:
        # the initial blocking nodes have no "origin node" nor cost
        board.nodes.came_from[block] = None
        board.nodes.cost_so_far[block]  = 0
    ############################################################################################
    # start pathfinding
    found = False
    # stops only when there are no longer any nodes to explore
    while not priority_queue.empty():
        current = priority_queue.get() # popping the node with highest priority
        # if the goal node has been retrieved from the queue, the goal has been found
        if current == goal:
            found = True
            break

        # generating all adjacent nodes
        neighbours:List[Tuple] = valid_adjacent_nodes(current, board)
        for next_node in neighbours:
            #cost of next node to goal
            new_cost:float = UNIT_COST + distance_to_goal(next_node, goal)
            # if the next node found is has no cost, or the new_cost is less than the current cost
            # record the new (lower) cost into the dictionary
            if next_node not in board.nodes.cost_so_far.keys() or new_cost < board.nodes.cost_so_far[next_node]:
                board.nodes.cost_so_far[next_node ] = new_cost
                priority:float = new_cost
                # placing node into the priority queue
                priority_queue.put(next_node , priority)
                board.nodes.came_from[next_node] = current

    # if all possible nodes have been explored, and the goal has not been found
    if (not found):
        print("Goal not found")
        exit(-1)    
    else:
        # prints the whole path taken to get to the goal
        find_print_path(board)

def find_print_path(board:Board):
    # getting the reversed path from goal
    curr_node = board.goal
    while (curr_node is not board.start):
        board.goal_path.insert(0, curr_node)
        curr_node = board.nodes.came_from[curr_node] 
    
    # last node retrieved will be the starting node
    board.goal_path.insert(0, curr_node)

    # prints the goal path tuples
    print(board.__str__())