from asyncio.windows_events import NULL
import heapq
from typing import TypeVar
from typing import List, Dict, Tuple

#priority queue class
T = TypeVar('T')
class PriorityQueue:
    
    #initialises the contents of the queue
    def __init__(self):
        self.elements: List[Tuple[float, T]] = []
    
    #checks if the queue is empty
    def empty(self) -> bool:
        return not self.elements
    
    #puts items into the queue based on its priority
    def put(self, item: T, priority: float):
        heapq.heappush(self.elements, (priority, item))
    
    #pops the item nearest to the goal that is unvisited
    def get(self) ->  T:
        return heapq.heappop(self.elements)[1]

#stores information on the nodes in the board
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
        
        # validating data
        # type checking
        if (type(self.size) is not int) or (type(self.start) is not list) or \
            (type(self.goal) is not list) or (type(data["board"]) is not list):
                exit("DataError in Board class: TypeError during Initialisation")

        #turning lists into tuples
        self.start = tuple(self.start)
        self.goal = tuple(self.goal)
        # range checking for nodes
        for i in [self.start[0], self.start[1], self.goal[0], self.goal[1]]:
            if (i>=self.size) or (i<0):
                exit("DataError in Board class: start/goal nodes not within the board")
        
        self.blocks = []
        for block_nodes in data["board"]:
            if (type(block_nodes) is list) and(len(block_nodes) == 3):
                block_tuple = tuple(block_nodes[1:3])
                x,y = block_tuple;
                if ((x<self.size) or (x>=0)) or ((y<self.size) or (y>=0)):
                    self.blocks.append(block_tuple)
                    continue
                exit("DataError in Board class: block_nodes (number error)")
            else:
                exit("DataError in Board class: block_nodes (formatting error)")

        self.nodes = Nodes() 





    
    
                

                                

    