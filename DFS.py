from Puzzle import Puzzle
from queue import LifoQueue
class DFS:
    def __init__(self,initial_state):
        self.board = initial_state
        
    def solve(self):
        root = self.board
        if not root.solvable():
            return ("The given puzzle is unsolvable"), 0
        if root.already_solved():
            return ("The given puzzle is already solved"),0
        
        queue = LifoQueue()
        queue.put(root)
        explored = []
        
        while not(queue.empty()):
            curr_state = queue.get()
            explored.append(curr_state.board)
            
            if curr_state.depth == 30: 
                continue
            child_states = curr_state.move()
            for c in child_states:
                if c.board not in explored:
                    if not c.solvable():
                        explored.append(c.board) # add unsolvable state to explored list
                        continue
                    if c.already_solved():
                        return c.solution(), len(explored)
                    queue.put(c)
                    
        return (("Unsolvable with the given depth"), len(explored))
            