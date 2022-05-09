import math
import random
from numpy import zeros

def scoring_system(player):
    
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
                    #calculate distance
        
        if (player.player == "red") and (n%2==1):
            board_score[(n/2,n/2)] = -100
        elif (player.player == "red"):
            board_score[(player.board.n, player.board.n)] = 100
        elif (player.player == "blue"):
            red_coord = player.last_coord
            if (red_coord[0]!= red_coord[1]  and player.count == 1):
                board_score[(red_coord[1],red_coord[0])] = "STEAL"
        else:
            #center pieces
            board_score[(n/2,n/2)] = 10
    # done initialising base scores   
    
    ## checking for blue's move, if threatens capture or long
    if (player.enemy_last_coord != (-1,-1)):
        threaten_capture = can_capture(player.enemy_last_coord, player, "defense")
        
        
        ## defend, update score board to prioritise defense
        enemy_list = player.board.connected_coords(player.enemy_last_coord)
        index_list = list(); index_list.append([]); index_list.append([])
        for node in enemy_list:
            index_list[0].append(node[player.player_goal])
            index_list[0].append(node[1-player.player_goal])

        if (max(index_list) - min(index_list)) <= math.floor(n/2):
            pass
            #threaten capture middle if possible, else just threaten capture the ends
            #check if any nodes capturable using function
        elif (max(index_list.count(index_list[0]))==n-1):
            # erecting barrier
            # looks for the empty spot in the barricade
            coord_list = list(set([i in range(0,n)])^set(index_list))
            coordinate = []; 
            coordinate[0]
            board_score[tuple(coordinate)]
    # 
    """

    ### utility function (MAX)
    # red vs blue pieces (red-blue) (ONLY THIS)
    board = player.board
    eval = 0
    if (player.player == "red"):
        eval += board.values().count("red") - board.values.count("blue")
        # length of goal path (positive)
        eval += len(player.goal_path)
    else:
        eval -= (board.values().count("blue") - board.values.count("red"))
        eval += len(player.goal_path)
    
    # distance to the either side
    if (player.board.connected_coords(player.last_coord) > player.max_path_length):
        player.max_path_length = player.board.connected_coords(player.last_coord)
    distance_to_goal(player.last_coord, player)




    
    # transposition table for all moves (branching factor is big)
    # blue captured = (+ score)
    # red captured = (negative -score)
    return 
# checks for nodes adjacent to the current node, and returns the valid ones
def valid_adjacent_nodes(current:tuple, player):
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
                valid_adj_nodes.append(tuple([x, y])) # converting to tuple to use as dictionary key
    return valid_adj_nodes

def distance_to_goal(current, player):
    goals = []
    a0, a1 = current[0], current[1]
    b0, b1
    if (player.player == "red"):
        goals =
        b0, b1 = goal[0], goal[1]

    x = b0 - a0
    y = b1 - a1
    
    dist = (abs(x) + abs(x + y) + abs(y)) / 2
    return dist

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
                adj_nodes.append(tuple(node)) # converting to tuple to use as dictionary key
    return adj_nodes

# def game_over(board, piece):
    
#     if piece == "red":
#         for i in range(board.n):
#             if board[0, i] == piece and board[board.n, i] == piece:
#                 return True
#     elif piece == "blue":
#         for i in range(board.n):
#             if board[i, 0] == piece and board[i, board.n] == piece:
#                 return True

def is_terminal_node(board):
	return game_over(board, PLAYER_PIECE) or game_over(board, AI_PIECE) or len(board.get_valid_locations(board)) == 0

def minimax(player, depth, alpha, beta):
    valid_locations = player.board.get_valid_locations
    board = player.board
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            return (None, 0)
        else: 
            # depth = 0
            return (None, player.scoring_system(player))

    # maximising player
    if player == "red":
        value = -math.inf
        node = random.choice(valid_locations)
        for valid in valid_locations:
            b_copy = board.copy()
            # place_piece(b_copy, valid, player)
            new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                node = valid
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return node, value

    else: # Minimizing player
        value = -math.inf
        node = random.choice(valid_locations)
        for valid in valid_locations:
            b_copy = board.copy()
            # place_piece(b_copy, valid, player)
            new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                node = valid
            beta = min(beta, value)
            if alpha >= beta:
                break
        return node, value

def pick_best_move(board, piece):

	valid_locations = player.board.get_valid_locations(board)
	best_score = -10000
	best = random.choice(valid_locations)
	for valid in valid_locations:
		temp_board = board.copy()
		place_piece(temp_board, valid, piece)
		score = scoring_system(temp_board, piece)
		if score > best_score:
			best_score = score
			best = valid

	return best

def place_piece(board, coord, piece):
    board[coord] = piece

def can_capture(node_to_place, player):
    board = player.board
    current = board[node_to_place]
    adj_nodes = generated_adj_nodes(current)
    
    # which enemy pieces get captured
    captured_boolean = False
    captured = list()

    # case 1
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

    # case 2



    



    return captured_boolean, [captured]