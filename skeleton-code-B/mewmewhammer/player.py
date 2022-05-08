import util
from turtle import distance
from mewmewhammer.board import Board
from numpy import zeros
# Actions
_ACTION_STEAL = "STEAL"
_ACTION_PLACE = "PLACE"

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
        self.size = n
        self.board = Board(n)
        self.count = 0;

        self.last_coord = (-1,-1)
        # self.transposition_table = dict() #apparently bad for storage requirements       
    
    
    
    
    def action(self):
        """
        Called at the beginning of your turn. Based on the current state
        of the game, select an action to play.
        """
        
        # put your code here    
        
        # #count
        # if self.board.digest not in self.transposition_table.keys():
        #     self.transposition_table[self.board.digest][0] +=1
        # else:
        #     self.transposition_table[self.board.digest] = [0,[]]
        #     self.transposition_table[self.board.digest][0] +=1
        #     self.transposition_table[self.board.digest][1] = self.scoring_system()
        

        # self.board.get_empty()

        if (self.player == "red" and self.count == 0): 
            action = ("PLACE", 1, 0)
            self.count += 1
        elif (self.player == "blue" and self.count == 0): 
            action = ("PLACE",0,0)
            self.count += 1
        elif (self.player == "red" and self.count == 1): 
            action = ("PLACE", 0, 1)
            self.count += 1
        elif (self.player == "blue" and self.count == 1): 
            action = ("PLACE",1,1)
            self.count += 1
        else:
            pass


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
            self.last_coord = (-1, -1)

        elif atype == _ACTION_PLACE:
            # Apply PLACE action
            coord = tuple(aargs)
            self.last_captures = self.board.place(player, coord)
            self.last_coord = coord
        else:
            # This should never happen, but good to be defensive
            raise self._illegal_action(action, f"Action not handled.")

        self.print_board()

   