# Board class
import numpy as np
import pygame
import pdb

class Board(object):
    def __init__(self):
        self.rows = 19
        self.cols = 19
        self.win_count = 5
        self.board = np.array([[0] * self.rows] * self.cols)
        self.game_run = True

    def check_win(self, token):
        # check horizontal
        for i in range(self.cols - self.win_count +1):
            for j in range(self.rows):
                if self.board[i][j] == token and self.board[i][j+1] == token and self.board[i][j+2] == token and self.board[i][j+3] == token and self.board[i][j+4] == token:
                    return True

        # check vertical
        for i in range(self.cols):
            for j in range(self.rows - self.win_count +1):
                if self.board[i][j] == token and self.board[i+1][j] == token and self.board[i+2][j] == token and self.board[i+3][j] == token and self.board[i+4][j] == token:
                    return True

        # check positive diagonal
        for i in range(self.cols - self.win_count +1):
            for j in range(self.rows - self.win_count +1):
                if self.board[i][j] == token and self.board[i+1][j+1] == token and self.board[i+2][j+2] == token and self.board[i+3][j+3] == token and self.board[i+4][j+4] == token:
                    return True

        #check negative diagonal
        for i in range(self.cols - self.win_count + 1):
            for j in range(self.rows):
                if self.board[i][j] == token and self.board[i-1][j+1] == token and self.board[i-2][j+2] == token and self.board[i-3][j+3] == token and self.board[i-4][j+4] == token:
                    return True

    def draw_board(self, window):
        pass









