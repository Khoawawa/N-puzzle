from Puzzle import Puzzle
from queue import LifoQueue
class DFS:
    def __init__(self,initial_state: Puzzle):
        self.board = initial_state
        
    def solve(self):
        root = self.board

        stack = LifoQueue()
        stack.put(root)
        
        explored = set()
        
        while not(stack.empty()):
            curr_state = stack.get()
            
            explored.add(curr_state)
            
            if curr_state.already_solved():
                return curr_state.solution(), len(explored)
            
            if not curr_state.solvable():
                continue
            
            # if curr_state.depth == 31: 
            #     continue
            
            child_states = curr_state.move()
            
            for c in child_states:
                if c not in explored:
                    stack.put(c)
                    
        return (("The initial board is unsolvable"), len(explored))
            