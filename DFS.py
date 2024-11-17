from Puzzle import Puzzle
from queue import LifoQueue
class DFS:
    def __init__(self,initial_state: Puzzle):
        self.board = initial_state
        
    def solve(self):
        root = self.board

        if not root.solvable():
            return 'The initial board is unsolvable', 0
        
        stack = LifoQueue()
        stack.put(root)
        
        explored = set()
        
        while not stack.empty():
            curr_state = stack.get()
            
            
            if curr_state.already_solved():
                return curr_state.solution(), len(explored)

            explored.add(curr_state)
            
            child_states = curr_state.move()
            
            for c in child_states:
                if c not in explored:
                    stack.put(c)
                    
        return (("No solution was found"), len(explored))
            