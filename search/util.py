"""
COMP30024 Artificial Intelligence, Semester 1, 2022
Project Part A: Searching

This module contains some helper functions for printing actions and boards.
Feel free to use and/or modify them to help you develop your program.
"""

from asyncio.windows_events import NULL
from fileinput import close
from itertools import islice
import math
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

def heuristic(current, goal):
    print(current)
    print(goal)
    x = ((current[0] - goal[0])**2)
    y = ((current[1] - goal[1])**2)
    distance = abs(math.sqrt(x+y))

    return distance

#checks for nodes adjacent to the current node, and returns the valid ones
def valid_adjacent_nodes(current, size, blocks):
    adj_nodes = generated_adj_nodes(current)
    valid_adj_nodes = []

    for node in adj_nodes:
        if node not in blocks:
            x,y = node[0], node[1]
            if not ((x >= size) or (y >= size) or (x < 0) or (y < 0)):
                valid_adj_nodes.append([x, y])
    print("VALID: " + str(valid_adj_nodes))
    return valid_adj_nodes
                

# generates a list of all adjacent nodes
def generated_adj_nodes(current):
    adj_nodes = []
    for y in [-1, 0, 1]:
        for x in [-1, 0, 1]:
            if y == x:
                continue
            else:
                node = []
                node.append(current[0]+x)
                node.append(current[1]+y)
                adj_nodes.append(node)

    return adj_nodes


# def min_distance_node(current, node_goal, size, blocks, close_nodes):
#     min_distance = 999999999 #replace with max limit
#     valid_nodes = valid_adjacent_nodes(current, size, blocks)
#     node = NULL
#     closest_node = NULL

#     if len(valid_nodes) == 0:
#         return NULL,NULL
    
#     # generates all the nodes, finds the node closest to the goal
#     for node in valid_nodes:
#         if node in close_nodes:
#             valid_nodes.remove(node)
#         else:
#             print("NODE: " + str(node))
#             goal_distance = UNIT_COST + heuristic(node, node_goal)
        
#             # the next closest node is the goal
#             if (goal_distance == UNIT_COST): return node, []

#             #finding min distance
#             if (goal_distance < min_distance):
#                 min_distance = goal_distance
#                 closest_node = node
                
#     # removes the closest node from the list, hence have the other open nodes to append
#     valid_nodes.remove(closest_node)

#     return closest_node, valid_nodes

def find_print_path(start:tuple, goal:tuple, came_from:dict):
    goal_path = list()
    curr_node = goal
    while (curr_node is not start):
        goal_path.insert(0, curr_node)
        curr_node = came_from[curr_node] 
    goal_path.insert(0, curr_node)

    print(str(len(goal_path)))
    for coor in goal_path:
        print(f"({coor[0]},{coor[1]})")
        