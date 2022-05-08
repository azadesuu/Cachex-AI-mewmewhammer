from turtle import distance
from referee import Board
from numpy import zeros
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
        self.transposition_table = dict() #apparently bad for storage requirements
         
    
    
    def scoring_system(self):
        board = self.board
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

            
            if (self.player == "red") and (n%2==1):
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
                    
        
    def action(self):
        """
        Called at the beginning of your turn. Based on the current state
        of the game, select an action to play.
        """
        # put your code here    
        
        #count
        if self.board.digest not in self.transposition_table.keys():
            self.transposition_table[self.board.digest][0] +=1
        else:
            self.transposition_table[self.board.digest] = [0,[]]
            self.transposition_table[self.board.digest][0] +=1
            self.transposition_table[self.board.digest][1] = self.scoring_system()

        

        self.board.get_empty()

        action = ("PLACE", 0, 0)
        return action

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
        # put your code here

    
