import math
import random
from numpy import zeros

def scoring_system(player):
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
            index_list = list()
            for node in enemy_list:
                index_list.append(node[player.player_goal])
            if (max(index_list) - min(index_list)) <= math.floor(n/2):
                pass
                #threaten capture middle if possible, else just threaten capture the ends
                #check if any nodes capturable using function


        ## update goal path (done in player)
            ## add points
        ## check the top valid locations for capture



        
            



        ## checking for next step in goal path



        # red will always start from 5,5
        # blue will always start from 0,n n,n n,0 n,n unless can capture


        valid_locations = player.board.get_valid_locations()
            

        # check if previous move threatens capture
        # else continue greedy algorithm

        return []
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

def distance_to_goal(current, goal):
    a0, a1 = current[0], current[1]
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
def can_capture(node_to_place, player, mode):
    # if mode == defense, node_to_place will be red's (aim to return false)
    # if mode = offense, node_to_place will be blue's (aim to return true)
    board = player.board

def is_terminal_node(player):
	return len(player.board.get_valid_locations()) == 0        

def minimax(player, depth, alpha, beta):
        valid_locations = player.board.get_valid_locations
        is_terminal = is_terminal_node(player)
        if depth == 0 or is_terminal:
            if is_terminal:
                return (None, 0)
            # depth = 0
            return (None, scoring_system(player))
    
        # maximising player
        if player == "red":
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
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