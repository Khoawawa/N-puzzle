from DFS import DFS
from Puzzle import Puzzle
import numpy as np
def main():
    k = 4
    initial_board = [[1,2,3,4],
                     [5,6,7,8],
                     [9,10,11,12],
                     [13,14,0,15]]
        
    init_puzzle = Puzzle(initial_board,k)
    
    #---PRINT INTIAL PUZZLE AND GOAL PUZZLE---#
    print("Initial state of the puzzle")
    print(init_puzzle)
    
    print("Goal state of the puzzle")
    print('\n'.join([' '.join(map(str,row)) for row in init_puzzle.goal]))
    #---PRINT SOLUTION---#
    print("Finding solution...")
    
    solver = DFS(init_puzzle)
    DFS_sol, explored_len = solver.solve()
    if isinstance(DFS_sol,list):
        print('DFS solution is: ')
        for step,state in enumerate(DFS_sol):
            print(f"Step {step}:\n{state}\n") 
    else:
        print(DFS_sol)
    print('Number of explored state is:', explored_len)
main()