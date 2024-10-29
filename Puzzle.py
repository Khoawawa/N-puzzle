import numpy as np
from copy import copy
# board should be sqrt(N+1)
class Puzzle:
    def __init__(self, board, k, depth=0):
        self.board = board
        self.goal = self.generateGoal(k)
        self.k = k
        self.depth = depth
        
    def already_solved(self):
        if self.board == self.goal:
            return True  
        return False
    
    def inv_num(self):
        flat_board = [num for row in self.board for num in row]
        
        inv = sum(1 for i in range(len(flat_board) - 1) for j in range(i+1,len(flat_board)) if flat_board[i] > flat_board[j] and flat_board[i] and flat_board[j]) 
        
        return inv
    
    def blank_row_from_bottom(self):
        for i, row in enumerate(reversed(self.board)):
            if 0 in row:
                return i+1
        return -1
    
    def solvable(self):
        inversions = self.inv_num()
        blank_row = self.blank_row_from_bottom()
        if self.k % 2 == 0:
            if blank_row % 2 ==0 and inversions % 2 != 0:
                return True
            if blank_row % 2 != 0 and inversions % 2 == 0:
                return True
        else:
            if inversions % 2 == 0:
                return True
        return False
                
    def generateGoal(self,k):
        e_size = k
        
        goal_state = [[1 + i + j*e_size for i in range(e_size)] for j in range(e_size)]
        goal_state[-1][-1] = 0
        
        return goal_state
    def find_blank_cell(self):
        for row in range(self.k):
            if 0 in self.board[row]:
                col = self.board[row].index(0)
                return (row,col)
        return None
    def legal_moves(self,x):
        moves = ['L','R','U','D']
        if x[1] == 0:
            moves.remove('L')
        if x[1] == self.k - 1:
            moves.remove('R')
        if x[0] == 0:
            moves.remove('U')
        if x[0] == self.k - 1:
            moves.remove('D')
        return moves
    def move(self):
        x = self.find_blank_cell()
        moves = self.legal_moves(x)
        
        children = []
        for direction in moves:
            temp_board = [row[:] for row in self.board]
            if direction == 'U':
                temp_board[x[0]][x[1]], temp_board[x[0] - 1][x[1]] = temp_board[x[0] - 1][x[1]], temp_board[x[0]][x[1]]
            elif direction == 'D':
                temp_board[x[0]][x[1]], temp_board[x[0] + 1][x[1]] = temp_board[x[0] + 1][x[1]], temp_board[x[0]][x[1]]
            elif direction == 'R':
                temp_board[x[0]][x[1]], temp_board[x[0]][x[1] + 1] = temp_board[x[0]][x[1] + 1], temp_board[x[0]][x[1]]
            elif direction == 'L':
                temp_board[x[0]][x[1]], temp_board[x[0]][x[1] - 1] = temp_board[x[0]][x[1] - 1], temp_board[x[0]][x[1]]
            children.append(Puzzle(temp_board,self.k,self.depth + 1))
        return children
        
        
if __name__ == "__main__":
    puzzle = Puzzle()