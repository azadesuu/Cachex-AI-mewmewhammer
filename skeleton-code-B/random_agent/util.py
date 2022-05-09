import math
import random
from numpy import zeros


def eval(b_copy, player, maximisingPlayer):

    # efficient
    # estimating utility
    # estimate who is going to win
    """
    board = player.board
    ### initialising##
    n = board.n
    # board empty
    if board._data == zeros((n, n), dtype=int):
        # choose maximum value
        # sets the value of each placement
        board_score = {(v,k):0 for (v,k) in range(0, n)}
        for i in range(0, n):
            for j in range (0,n):
                if (i==0) and (j==5):
                    # cannot be swapped
                    board_score = 10
                if (i == j):
                    board_score[(i,j)] = 5
                    # calculate distance
                elif (i == 0) or (j==0):
                    board_score[(i,j)] = 5
                else:
                    pass
                    # calculate distance

        if (player.player == "red") and (n%2==1):
            board_score[(n/2,n/2)] = -100
        elif (player.player == "red"):
            board_score[(player.board.n, player.board.n)] = 100
        elif (player.player == "blue"):
            red_coord = player.last_coord
            if (red_coord[0]!= red_coord[1]  and player.count == 1):
                board_score[(red_coord[1],red_coord[0])] = "STEAL"
        else:
            # center pieces
            board_score[(n/2,n/2)] = 10
    # done initialising base scores

    # checking for blue's move, if threatens capture or long
    if (player.enemy_last_coord != (-1,-1)):
        threaten_capture = can_capture(
            player.enemy_last_coord, player, "defense")


        # defend, update score board to prioritise defense
        enemy_list = player.board.connected_coords(player.enemy_last_coord)
        index_list = list(); index_list.append([]); index_list.append([])
        for node in enemy_list:
            index_list[0].append(node[player.player_goal])
            index_list[0].append(node[1-player.player_goal])

        if (max(index_list) - min(index_list)) <= math.floor(n/2):
            pass
            # threaten capture middle if possible, else just threaten capture the ends
            # check if any nodes capturable using function
        elif (max(index_list.count(index_list[0]))==n-1):
            # erecting barrier
            # looks for the empty spot in the barricade
            coord_list = list(set([i in range(0,n)])^set(index_list))
            coordinate = [];
            coordinate[0]
            board_score[tuple(coordinate)]
    #
    """

    # utility function (MAX)
    # red vs blue pieces (red-blue) (ONLY THIS)
    board = b_copy
    coord = player.last_test
    eval = 0
    min_distance = distance_to_goal(coord, player)
    steal = False
    if (player.player == "red"):
        if (coord[0] == coord[1]) and (coord[0] == math.floor(board.n/2)) and (board.n % 2 == 1):
            # odd number
            return (-math.inf, None)
        if (coord[0] == coord[1]):
            eval+=1
        eval += board.count("red") - board.count("blue")
        # length of goal path (positive)
        eval += len(board.connected_coords(coord))
        # distance to either side
        eval += board.n - min_distance
        # if (can_capture(coord)):
        #     eval += 2

    else:
        if (player.count == 1):
            red_coord = board.get_first_token("red")
            if(red_coord[0] != red_coord[1]):
                eval -= 1
                player.count += 1
                steal = True
        if (coord[0] == coord[1]):
            eval-=1
        eval -= (board.count("blue") - board.count("red"))
        eval -= len(board.connected_coords(coord))
        eval -= (player.board.n - min_distance)
        # if (can_capture(coord)):
        #     eval -= 2

    # transposition table for all moves (branching factor is big)
    # blue captured = (+ score)
    # red captured = (negative -score)
    return (eval, steal)
# checks for nodes adjacent to the current node, and returns the valid ones


def valid_adjacent_nodes(current: tuple, player):
    board = player.board
    # generating all adjacent nodes
    adj_nodes = generated_adj_nodes(current)
    # stores only valid adjacent nodes
    valid_adj_nodes = []
    for node in adj_nodes:
        if node not in board.blocks:
            x, y = node[0], node[1]
            # checking if the numbers are within bounds
            if not ((x >= board.size) or (y >= board.size) or (x < 0) or (y < 0)):
                # converting to tuple to use as dictionary key
                valid_adj_nodes.append(tuple([x, y]))
    return valid_adj_nodes


def distance_to_goal(current, player):
    a0, a1 = current[0], current[1]
    b0, b1 = 0, 0
    goals_1 = list()
    goals_2 = list()
    distances = list()
    if (player.player == "red"):
        goals_1 = [(0, n) for n in range(0, player.board.n)]
        goals_2 = [(player.board.n-1, n) for n in range(0, player.board.n)]
    elif (player.player == "blue"):
        goals_1 = [(n, 0) for n in range(0, player.board.n)]
        goals_2 = [(n, player.board.n-1) for n in range(0, player.board.n)]

    for b0, b1 in goals_1+goals_2:
        x = b0 - a0
        y = b1 - a1
        distances.append((abs(x) + abs(x + y) + abs(y)) / 2)

    return min(distances)


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
                node.append(current[0] + x)
                node.append(current[1] + y)
                # converting to tuple to use as dictionary key
                adj_nodes.append(tuple(node))
    return adj_nodes


def game_over(board, piece):
    if piece == "red":
        for i in range(board.n):
            if board[(0, i)] == piece and len(board.connected_coords((0, i))) >= board.n:
                for j in range(board.n):
                    if board[(board.n-1, j)] == piece:
                        return True
    elif piece == "blue":
        for i in range(board.n):
            if board[(i, 0)] == piece and len(board.connected_coords((i, 0))) >= board.n:
                for j in range(board.n):
                    if board[(j, board.n-1)] == piece:
                        return True


def is_terminal_node(player):
    return game_over(player.board, player.player) or len(player.board.get_valid_locations()) == 0


def minimax(b_copy, player, depth, alpha, beta, maximisingPlayer):
    valid_locations = b_copy.get_valid_locations()
    is_terminal = is_terminal_node(player)
    steal = False
    chosen_coord = None
    if depth == 0 or is_terminal:
        if game_over(player.board, player.player):
            if player.player == "red":
                return (None, (100000000000000, None))
            elif player.player == "blue":
                return (None, (-10000000000000,None))
            else:  # Game is over, no more valid moves
                return (None, (0, None))
        else:
            # Depth is zero
            return (None, eval(b_copy, player, maximisingPlayer))
    if maximisingPlayer:
        value = -math.inf
        for coord in valid_locations:
            b_copy[coord] = "red"
            player.last_test = coord
            result = minimax(b_copy, player, depth-1, alpha, beta, False)
            new_score = result[1][0]
            steal = result[1][1]
            if new_score > value:
                value = new_score
                chosen_coord = coord
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return (chosen_coord, (value, steal))

    else:  # Minimizing player
        value = math.inf
        for coord in valid_locations:
            b_copy[coord] = "blue"
            player.last_test = coord
            result = minimax(b_copy, player, depth-1, alpha, beta, True)
            new_score = result[1][0]
            steal = result[1][1]
            if new_score < value:
                value = new_score
                chosen_coord = coord
            beta = min(beta, value)
            if alpha >= beta:
                break
        return (chosen_coord, (value, steal))


def place_piece(board, coord, piece):
    board[coord] = piece


def can_capture(node_to_place, player):
    board = player.board
    adj_nodes = generated_adj_nodes(board[node_to_place])

    # which enemy pieces get captured
    captured_boolean = False
    captured = list()

    if player == "red":
        opp_player = "blue"

    for node in adj_nodes:
        if board[node] == player:
            # next =
            pass
        elif board[node] == opp_player:
            first = adj_nodes[0]
            last = adj_nodes[-1]
            current = adj_nodes[0]
            for next in adj_nodes[1:]:
                if next != last:
                    if current != player and next != player:
                        adj_first = generated_adj_nodes(current)
                        adj_sec = generated_adj_nodes(next)
                        for first_coord in adj_first:
                            for sec_coord in adj_sec:
                                if (first_coord == sec_coord) and (first_coord != node_to_place):
                                    if first_coord == player:
                                        captured_boolean = True
                                        captured.append(current)
                                        captured.append(next)

                else:
                    if last != player and first != player:
                        adj_first = generated_adj_nodes(last)
                        adj_sec = generated_adj_nodes(first)
                        for first_coord in adj_first:
                            for sec_coord in adj_sec:
                                if (first_coord == sec_coord) and (first_coord != node_to_place):
                                    if first_coord == player:
                                        captured_boolean = True
                                        captured.append(last)
                                        captured.append(first)
                current = next

    return captured_boolean, [captured]
