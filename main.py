from DFS import DFS
from Puzzle import Puzzle
import numpy as np
def main():
    n = int(input('Enter desired N-puzzle: '))
    k = int(np.sqrt(n+1))
    initial_board = []
    
    for _ in range(k):
        row = list(map(int, input().strip().split()))
        initial_board.append(row)
        
    init_puzzle = Puzzle(initial_board,k)
    solver = DFS(init_puzzle)
    DFS_sol, explored_len = solver.solve()
    if isinstance(DFS_sol,list):
        print('DFS solution is:',end=' ')
        for step in DFS_sol:
            print(step,end=' ') 
        print('')
    else:
        print(DFS_sol)
    print('Number of explored state is: ', explored_len)
main()