import numpy as np
from copy import copy
import random
# board should be sqrt(N+1)
class Puzzle:
    def __init__(self, board, k, direction=None,depth=0,parent=None):
        self.k = k
        if board:
            self.board = board
        else:
            self.generateRandomBoard(k)
        self.goal = self.generateGoal(k)
        self.depth = depth
        self.parent = parent
        self.direction = direction
    
    def generateRandomBoard(self,k):
        while True:
            board_1d = list(range(1, k*k)) + [0]
            random.shuffle(board_1d)
            self.board = [board_1d[i * k : (i+1) * k] for i in range(k)]
            if self.solvable():
                break
            
    def already_solved(self):
        return self.board == self.goal
    
    def _count_and_merge(self,arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        
        left = arr[l : m + 1]
        right = arr[m + 1: r + 1]
        
        res = 0
        i = 0
        j = 0
        k = l
        
        while i < n1 and j < n2:

        # No increment in inversion count
        # if left[] has a smaller or equal element
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
                res += (n1 - i)
            k += 1

        # Merge remaining elements
        while i < n1:
            arr[k] = left[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = right[j]
            j += 1
            k += 1

        return res
            
    def _count_inv(self,arr,l,r):
        res = 0
        if l < r:
            m = (r + l) // 2

            res += self._count_inv(arr,l,m)
            res += self._count_inv(arr, m + 1, r)
            
            res += self._count_and_merge(arr, l, m, r)
        return res
    
    def inv_num(self):
        flat_board = [num for row in self.board for num in row if num != 0]
        return self._count_inv(flat_board,0, len(flat_board) - 1)
        # inv = 0
        # for i in range(len(flat_board)-1):
        #     for j in range(i+1 , len(flat_board)):
        #         if ((flat_board[i] > flat_board[j]) and flat_board[i] and flat_board[j]):
        #             inv += 1   
        # # inv = sum(1 for i in range(len(flat_board) - 1) for j in range(i+1,len(flat_board)) if flat_board[i] > flat_board[j] and flat_board[i] and flat_board[j]) 
        
        # return inv
    
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
                return row,col
        return None
    
    def legal_moves(self,row,col):
        moves = ['L','R','D','U']
        if col == 0:
            moves.remove('L')
        if col == self.k - 1:
            moves.remove('R')
        if row == 0:
            moves.remove('U')
        if row == self.k - 1:
            moves.remove('D')
            
        return moves
    
    def _swap_cell(self, r1, c1, r2, c2):
        new_board = [row[:] for row in self.board]
        new_board[r1][c1], new_board[r2][c2] = new_board[r2][c2], new_board[r1][c1]
        
        return new_board
    
    def move(self):
        x_row,x_col = self.find_blank_cell()
        moves = self.legal_moves(x_row,x_col)
        
        children = []
        new_board = None
        
        for direction in moves:
            new_row = x_row
            new_col = x_col
            
            if direction == 'U':
                new_row = x_row - 1
            elif direction == 'D':
                new_row = x_row + 1
            elif direction == 'R':
                new_col = x_col + 1
            elif direction == 'L':
                new_col = x_col - 1
                
            new_board = self._swap_cell(x_row,x_col,new_row,new_col)
            
            children.append(Puzzle(new_board,self.k,direction,self.depth + 1,self))
        
        return children
    
    def solution(self):
        sol =[]
        sol.append(self)
        path = self
        
        while(path.parent):
            path = path.parent  
            sol.append(path)
        
        sol.reverse()
        
        return sol
    
    def __eq__(self, other):
        return self.board == other.board
    
    def __str__(self):
        return '\n'.join([' '.join(map(str,row)) for row in self.board])
    
    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.board))
