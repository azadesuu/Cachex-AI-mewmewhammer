from search.classes import T
import util
import math
from turtle import distance
from mewmewhammer.board import Board
from util import minimax
# Actions
_ACTION_STEAL = "STEAL"
_ACTION_PLACE = "PLACE"
_ROW = 0
_COL = 1

# Action type validators
_ACTION_TYPES = set([
    (_ACTION_STEAL, ), 
    (_ACTION_PLACE, int, int)
])
class Player:

    def __init__(self, player, n):
        """
        Called once at the beginning of a game to initialise this player.
        Set up an internal representation of the game state.

        The parameter player is the string "red" if your player will
        play as Red, or the string "blue" if your player will play
        as Blue.
        """
        
        self.player = player
        self.player_goal = _ROW if (player =="red") else _COL

        self.size = n
        self.board = Board(n)
        self.count = 0
        self.last_action = tuple()s

        self.last_coord = (-1,-1)
        self.enemy_last_coord = (-1,-1)
        # self.transposition_table = dict() #apparently bad for storage requirements       
    
    
    
    
    def action(self):
        """
        Called at the beginning of your turn. Based on the current state
        of the game, select an action to play.
        """
        
        # put your code here 
        maximisingPlayer = False
        if self.player == "red":
            maximisingPlayer = True

        coord, minimax_score, steal = minimax(self.board, 3, -math.inf, math.inf, maximisingPlayer)


        return action
    

    def print_board(self):
        node_list = []
        count = 0
        for i in reversed(range(0,self.board.n)):
            node_list.append([])
            for j in range(0, self.board.n):
                node_list[count].append(self.board[(i,j)])
            print(node_list[count])
            count +=1


    def turn(self, player, action):
        """
        Called at the end of each player's turn to inform this player of 
        their chosen action. Update your internal representation of the 
        game state based on this. The parameter action is the chosen 
        action itself. 
        
        Note: At the end of your player's turn, the action parameter is
        the same as what your player returned from the action method
        above. However, the referee has validated it at this point.
        """
        atype, *aargs = action
        action_type = (atype, *(type(arg) for arg in aargs))
        if not isinstance(atype, str) or action_type not in _ACTION_TYPES:
            self._illegal_action(action,
                f"Action does not exist or is not well formed."
            )

        # Validate/apply action based on type
        if atype == _ACTION_STEAL:
            # Apply STEAL action
            self.board.swap()
            self.last_coord = (self.enemy_last_coord[1], self.enemy_last_coord[0])
            self.enemy_last_coord = (-1,-1)

        elif atype == _ACTION_PLACE:
            # Apply PLACE action
            coord = tuple(aargs)
            self.last_captures = self.board.place(player, coord)
            if (player == self.player):
                self.last_coord = coord
            else:
                self.enemy_last_coord = coord
        else:
            # This should never happen, but good to be defensive
            raise self._illegal_action(action, f"Action not handled.")
        self.last_action = action
        player.last_action = action
        self.print_board()

   