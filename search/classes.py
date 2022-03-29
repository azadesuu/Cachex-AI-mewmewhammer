from asyncio.windows_events import NULL
import heapq
from typing import TypeVar
from typing import Tuple, List

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

#board class, getattr(object, 'attribute')
class Board:
    def __init__(self, data):
        # size of board
        self.size: int = data["n"]
        # start and end nodes
        self.start: List = data["start"]
        self.goal: List = data["goal"]
        print(type(data["n"]))
        # validating data
        # type checking
        if (type(self.size) is not int) or (type(self.start) is not List) or \
            (type(self.goal) is not List) or (type(data["board"]) is not List):
                exit("DataError in Board class: TypeError during Initialisation")
        # range checking for nodes
        for i in [self.start[0], self.start[1], self.goal[0], self.goal[1]]:
            if (i>=self.size) or (i<0):
                exit("DataError in Board class: start/goal nodes not within the board")
        
        self.blocks = []
        for block_nodes in data["board"]:
            if (type(block_nodes) is list) and(len(block_nodes) == 3):
                block_tuple = block_nodes[1:3]
                for j in [block_tuple[0], block_tuple[1]]:
                    if (j>=self.size) or (j<0):
                        self.blocks.append(block_tuple)
                        continue
                    exit("DataError in Board class: block_nodes (number error)")
            exit("DataError in Board class: block_nodes (formatting error)")
    
                

                                

    