from DFS import DFS
from Puzzle import Puzzle
def main():
    k = 3
    initial_board = [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 0]]
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