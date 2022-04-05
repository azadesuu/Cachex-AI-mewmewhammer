import heapq
from typing import TypeVar
from typing import List, Dict, Tuple

#priority queue class
T = TypeVar('T')
class PriorityQueue:
    # initialises the contents of the queue
    # float is the priority, T is the item
    def __init__(self):
        self.elements: List[Tuple[float, T]] = []
    
    # checks if the queue is empty
    def empty(self) -> bool:
        return len(self.elements) <=0
    
    # puts items into the queue based on its priority
    def put(self, item: T, priority: float):
        heapq.heappush(self.elements, (priority, item))
    
    # pops the item nearest to the goal that is unvisited
    def get(self) ->  T:
        return heapq.heappop(self.elements)[1]

# stores information on the nodes in the board
class Nodes:
    def __init__(self):
        # stores the previous location of a given location tuple
        self.came_from: Dict[Tuple, Tuple] = dict()
        # stores the cost of a given location
        self.cost_so_far: Dict[Tuple, float] = dict()

# board class, contains size, starting node, goal node, and the existing 'blocking' nodes
class Board:
    def __init__(self, data):
        # size of board
        self.size: int = data["n"]

        # start and end nodes
        self.start: List = data["start"]
        self.goal: List = data["goal"]
        self.blocks = []
        
        self.nodes = Nodes() 
        self.goal_path = list()
        self.board = dict()
        
        ##################### DATA VALIDATION ############################
        # type checking
        if (type(self.size) is not int) or (type(self.start) is not list) or \
            (type(self.goal) is not list) or (type(data["board"]) is not list):
                exit("DataError in Board class: TypeError during Initialisation")

        # turning lists into tuples for dictionary key reasons
        self.start = tuple(self.start)
        self.goal = tuple(self.goal)
        # range checking for nodes
        for i in [self.start[0], self.start[1], self.goal[0], self.goal[1]]:
            if (i>=self.size) or (i<0):
                exit("DataError in Board class: start/goal nodes not within the board")

        # checking if node blocks are valid
        for block_nodes in data["board"]:
            if (type(block_nodes) is list) and(len(block_nodes) == 3):
                block_tuple = tuple(block_nodes[1:3])
                x,y = block_tuple
                if ((x < self.size) or (x >= 0)) or ((y < self.size) or (y >= 0)):
                    self.blocks.append(block_tuple)
                    continue
                exit("DataError in Board class: block_nodes (number error)")
            else:
                exit("DataError in Board class: block_nodes (formatting error)")
        ################################# END #############################

        # updating board.board attribute
        for node in self.blocks:
            self.board[node] = "b"
        self.board[self.start] = "s"
        self.board[self.goal] = "g"


    def __str__(self):
        string = ''
        string += str(len(self.goal_path))
        for coor in self.goal_path:
            string += (f"\n({coor[0]},{coor[1]})")
        return string
            
        





    
    
                

                                

    