import tkinter as tk
from tkinter import messagebox
import copy

import copy
class Board():
    def __init__(self,matrix,type):
        self.matrix = matrix
        self.type = type
        self.eval = 0
        self.depth = 0
        self.children = []
        self.free_spaces = []
        
    def freespace(self):
        i = 0
        j = 0
        for i in range(0,3):
            for j in range(0,3):
                if self.matrix[i][j] == ' ':
                    if (i,j) not in self.free_spaces:
                        self.free_spaces.append((i,j))
    def successors(self):
        self.freespace()
        if self.type == 1:
            for tup in self.free_spaces:
                child = None
                child = copy.deepcopy((self.matrix))
                child[tup[0]][tup[1]] = 'O'
                a_child = Board(child,0)
                a_child.depth = self.depth + 1
                self.children.append(a_child)
        else:        
            for tup in self.free_spaces:
                child = None
                child = copy.deepcopy((self.matrix))
                child[tup[0]][tup[1]] = 'X'
                a_child = Board(child,1)
                a_child.depth = self.depth + 1
                self.children.append(a_child)
                
    def goal_test(self):
        
        def row_check(r1,r2,r3):
            t = ' '
            d = 0
            if (r1[0] == r1[1] == r1[2] == 'X') or r1[0] == r1[1] == r1[2] == 'O':
                t = r1[0]
                
                d = 1
                return d
            elif (r2[0] == r2[1] == r2[2] == 'X') or (r2[0] == r2[1] == r2[2] == 'O'):
                t = r2[0]
                
                d = 1 
                return d
            elif (r3[0] == r3[1] == r3[2] == 'X') or (r3[0] == r3[1] == r3[2] == 'O'):
                t = r3[0]
                
                d = 1
                return d
        def column_check(r1,r2,r3):
            t = ' '
            d = 0
            if (r1[0] == r2[0] == r3[0] == 'X') or (r1[0] == r2[0] == r3[0] == 'O'):
                t = r1[0]
                
                d = 1
                return d
            elif (r1[1] == r2[1] == r3[1] == 'X') or (r1[1] == r2[1] == r3[1] == 'O'):
                t = r1[1]
                
                d = 1
                return d
            elif (r1[2] == r2[2] == r3[2] == 'X') or (r1[2] == r2[2] == r3[2] == 'O'):
                t = r3[2]
                
                d = 1
                return d
        def diagonal_check(r1,r2,r3):
            t = ' '
            d = 0
            if (r1[0] == r2[1] == r3[2] == 'X') or (r1[0] == r2[1] == r3[2] == 'O'):
                t = r1[0]
                d = 1
                return d
            elif (r1[2] == r2[1] == r3[0] == 'X') or (r1[2] == r2[1] == r3[0] == 'O'):
                t = r1[2]
                
                d = 1 
                return d
        def game_check(r1,r2,r3):
            
            d1 = 0
            d2 = 0
            d3 = 0
            d1 = row_check(r1,r2,r3)
            d2 = column_check(r1,r2,r3)
            d3 = diagonal_check(r1,r2,r3)
            return (d1 or d2 or d3)
        winner = ' '
        if game_check(self.matrix[0],self.matrix[1],self.matrix[2]):
                    
            if self.type == 1:
                winner = 'X'
            else:
                winner = 'O'
        return winner

    def evaluation(self):
        if self.goal_test() == 'X':
            self.eval = float('-inf')
            return
        elif self.goal_test() == 'O':
            self.eval = float('inf')
            return
        else:
            def o_eval(self):
                def freq(a,lis):
                    fre = 0
                    for i in lis:
                        if i == a:
                            fre += 1
                    return fre
                def rcd_eval(l):
                    rcd = 0
                    if l[0] == l[1] == l[2] == ' ':
                        rcd = rcd + 1
                    elif 'O' in l:
                        if 'X' in l:
                            rcd = 0
                            return rcd
                        else:
                            if freq('O',l) == 2:
                                rcd = rcd + 100
                            elif freq('O',l) == 1:
                                rcd = rcd + 10
                    return rcd
                e1 = rcd_eval(self.matrix[0])
                e2 = e1 + rcd_eval(self.matrix[1])
                e3 = e2 + rcd_eval(self.matrix[2])
                e4 = e3 + rcd_eval([self.matrix[0][0],self.matrix[1][0],self.matrix[2][0]])
                e5 = e4 + rcd_eval([self.matrix[0][1],self.matrix[1][1],self.matrix[2][1]])
                e6 = e5 + rcd_eval([self.matrix[0][2],self.matrix[1][2],self.matrix[2][2]])
                e7 = e6 + rcd_eval([self.matrix[0][0],self.matrix[1][1],self.matrix[2][2]])
                e8 = e7 + rcd_eval([self.matrix[2][0],self.matrix[1][1],self.matrix[0][2]])
                return e8
            def x_eval(self):
                def freq(a,lis):
                    fre = 0
                    for i in lis:
                        if i == a:
                            fre += 1
                    return fre
                def rcd_eval(l):
                    rcd = 0
                    if l[0] == l[1] == l[2] == ' ':
                        rcd = rcd + 1
                    elif 'X' in l:
                        if 'O' in l:
                            rcd = 0
                            return rcd
                        else:
                            if freq('X',l) == 2:
                                rcd = rcd + 3
                            elif freq('X',l) == 1:
                                rcd = rcd + 2
                    return rcd
                e1 = rcd_eval(self.matrix[0])
                e2 = e1 + rcd_eval(self.matrix[1])
                e3 = e2 + rcd_eval(self.matrix[2])
                e4 = e3 + rcd_eval([self.matrix[0][0],self.matrix[1][0],self.matrix[2][0]])
                e5 = e4 + rcd_eval([self.matrix[0][1],self.matrix[1][1],self.matrix[2][1]])
                e6 = e5 + rcd_eval([self.matrix[0][2],self.matrix[1][2],self.matrix[2][2]])
                e7 = e6 + rcd_eval([self.matrix[0][0],self.matrix[1][1],self.matrix[2][2]])
                e8 = e7 + rcd_eval([self.matrix[2][0],self.matrix[1][1],self.matrix[0][2]])
                return e8
            self.eval = o_eval(self) - x_eval(self)
            
        
    def draw_test(self):
        self.freespace()
        if len(self.free_spaces) == 0 and  self.goal_test() == ' ':
            return 1
        else:
            return 0
    def __str__(self):
        return f"{self.matrix[0]}\n{self.matrix[1]}\n{self.matrix[2]}\n"
max_depth = 5
def maximum(lis):
    max = float('-inf')
    for ele in lis:
        if ele > max:
            max = ele
    return max
def minimum(lis):
    min = float('inf')
    for ele in lis:
        if ele < min:
            min = ele
    return min
def Max(node):
    global max_depth
    if node.goal_test() == 'X':
        node.eval = float('-inf')
        return node.eval
    elif node.goal_test() == 'O':
        node.eval = float('inf')
        return node.eval
    elif node.draw_test():
        node.eval = 0
        return node.eval
    elif node.depth == max_depth:
        node.evaluation()
        return node.eval
    else:
        
        node.successors()
        child_utils = []
        for child in node.children:
            child_utils.append(Min(child))
        node.eval = maximum(child_utils)
        return node.eval
def Min(node):
    global max_depth
    if node.goal_test() == 'O':
        node.eval = float('inf')
        return node.eval
    elif node.goal_test() == 'X':
        node.eval = float('-inf')
        return node.eval
    elif node.draw_test():
        node.eval = 0
        return node.eval
    elif node.depth == max_depth:
        node.evaluation()
        return node.eval
    else:
        
        node.successors()
        child_utils = []
        for child in node.children:
            child_utils.append(Max(child))
        node.eval = minimum(child_utils)
        return node.eval


class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = 'X'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.board_matrix = [[' ' for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text=" ", width=10, height=3,
                                   font=('Arial', 20),
                                   command=lambda i=i, j=j: self.player_move(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def player_move(self, i, j):
        if self.buttons[i][j]["text"] == " ":
            self.buttons[i][j]["text"] = 'X'
            self.board_matrix[i][j] = 'X'
            if self.check_winner(self.board_matrix, 'X'):
                messagebox.showinfo("Game Over", "X wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.ai_move()

    def ai_move(self):
        next_board = Board(self.board_matrix, 1)
        max_eval = Max(next_board)
        for child in next_board.children:
            if child.eval == max_eval:
                break
        self.board_matrix = child.matrix
        self.update_ui()
        
        if child.goal_test() == 'O':
            messagebox.showinfo("Game Over", "O wins!")
            self.reset_game()
        elif self.check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_game()

    def update_ui(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = self.board_matrix[i][j]

    def check_winner(self, board, player):
        # Check rows, columns, and diagonals for a winner
        for row in board:
            if row == [player] * 3:
                return True
        for col in range(3):
            if [board[row][col] for row in range(3)] == [player] * 3:
                return True
        if [board[i][i] for i in range(3)] == [player] * 3 or \
           [board[i][2 - i] for i in range(3)] == [player] * 3:
            return True
        return False

    def check_draw(self):
        return all(self.board_matrix[i][j] != ' ' for i in range(3) for j in range(3))

    def reset_game(self):
        self.board_matrix = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = " "

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeApp(root)
    root.mainloop()
