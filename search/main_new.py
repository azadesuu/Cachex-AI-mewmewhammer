import heapq

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
    def get(self) -> T:
        return heapq.heappop(self.elements)[1]


def main_new(start, goal):
    ###################################IMPORTING DATA#########################################
    try:
        with open(sys.argv[1]) as file:
            data = json.load(file)      
    except IndexError:
        print("usage: python3 -m search path/to/input.json", file=sys.stderr)
        sys.exit(1)
    
    # board dimensions
    board_size = data["n"]
    #putting in closed nodes (cannot be visited)
    blocks = []
    for block_nodes in data["board"]:
        blocks.append(block_nodes[1:3])

    node_start = tuple(data["start"])
    node_goal = tuple(data["goal"])
    ############################################################################################
    ###################################INITIALISING DATA########################################
    
    frontier = PriorityQueue()
    frontier.put(start, 0)
    # stores the previous location of a given location tuple
    came_from = dict()
    # stores the cost of a given location
    cost_so_far = dict()
    came_from[node_start] = None
    cost_so_far[node_start] = 0
    ############################################################################################
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next, goal)
                frontier.put(next, priority)
                came_from[next] = current
    
    return came_from, cost_so_far

