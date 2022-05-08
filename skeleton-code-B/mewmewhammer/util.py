import math
import random
from numpy import zeros

def scoring_system(player):
        board = player.board
        # initialising
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
            else:
                board_score[(n/2,n/2)] = 10
        # done initialising base scores
        # check for captures
        for i in [(0,1),(1,0),(1,1),(-1,0),(0,-1),(-1,-1)]:
            break

        # checking for 
        # check if previous move threatens capture
        # else continue greedy algorithm

        return []

def is_terminal_node(board):
	return winning_move(board, PLAYER_PIECE) or winning_move(board, AI_PIECE) or len(get_valid_locations(board)) == 0

def minimax(player, depth, alpha, beta):
        valid_locations = player.board.get_valid_locations
        is_terminal = is_terminal_node(board)
        if depth == 0 or is_terminal:
            if is_terminal:
                if winning_move(player.board, AI_PIECE):
                    return (None, math.inf)
                elif winning_move(player.board, PLAYER_PIECE):
                    return (None, -math.inf)
                else: # Game is over, no more valid moves
                    return (None, 0)
            else: # Depth is zero
                return (None, player.scoring_system(board))
    
        # maximising player
        if player == "red":
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = get_next_open_row(board, col)
                b_copy = board.copy()
                drop_piece(b_copy, row, col, AI_PIECE)
                new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value

        else: # Minimizing player
            value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = get_next_open_row(board, col)
                b_copy = board.copy()
                drop_piece(b_copy, row, col, PLAYER_PIECE)
                new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value

def pick_best_move(board, piece):

	valid_locations = get_valid_locations(board)
	best_score = -10000
	best_col = random.choice(valid_locations)
	for col in valid_locations:
		row = get_next_open_row(board, col)
		temp_board = board.copy()
		drop_piece(temp_board, row, col, piece)
		score = score_position(temp_board, piece)
		if score > best_score:
			best_score = score
			best_col = col

	return best_col