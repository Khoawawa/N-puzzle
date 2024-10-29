from DFS import DFS
from Puzzle import Puzzle
def main():
    k = 3
    initial_board = [[1, 2, 3],
                     [4, 5, 6],
                     [7, 0, 8]]
    init_puzzle = Puzzle(initial_board,k)
    solver = DFS(init_puzzle)
    print(solver.solve())
main()