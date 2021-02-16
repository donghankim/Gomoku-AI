from player import Player
import numpy as np
import random
from copy import deepcopy
import pdb


class Naiive(Player):
    def __init__(self, config, name, token):
        super().__init__(config, name, token)

    def make_move(self, curr_player, wait_player, board):
        recent_x = wait_player.history[-1][0]
        recent_y = wait_player.history[-1][1]

        while True:
            random_x = random.randint(recent_x-1, recent_x+1)
            random_y = random.randint(recent_y-1, recent_y+1)
            if self.valid_move(random_x, random_y, board):
                return random_x, random_y


class Heuristic(Player):
    def __init__(self, config, name, token):
        super().__init__(config, name, token)
        self.north_score = 0
        self.east_score = 0
        self.south_score = 0
        self.west_score = 0
        self.ne_score = 0
        self.se_score = 0
        self.sw_score = 0
        self.nw_score = 0


    def make_move(self, curr_player, wait_player, board):
        recent_x = wait_player.history[-1][0]
        recent_y = wait_player.history[-1][1]

        states = np.zeros_like(board.board)
        for row in range(board.board.shape[0]):
            for col in range(board.board.shape[1]):
                if board.board[row][col] == curr_player.token:
                    states[row][col] = -1*curr_player.token
                elif board.board[row][col] == wait_player.token:
                    states[row][col] == -1*wait_player.token
                else:
                    states[row][col] = self.evaluate(row, col, board.board)

        print(board.board)
        print(states)
        max_idx = np.unravel_index(states.argmax(), states.shape)
        row_move = max_idx[0]
        col_move = max_idx[1]

        while True:
            if self.valid_move(row_move, col_move, board):
                break
            else:
                row_move += 1

        return row_move, col_move


    def north_search(self, row, col, search_area):
        score = 0
        for i in range(5):
            if row-i == -1:
                break
            elif search_area[row-i][col] == self.token:
                score += 1

        if score == 5:
            return 1000
        else:
            return score

    def ne_search(self, row, col, search_area):
        score = 0
        for i in range(5):
            if col+i == search_area.shape[1] or row-i == -1:
                break
            elif search_area[row-i][col+i] == self.token:
                score += 1

        if score == 5:
            return 1000
        else:
            return score

    def east_search(self, row, col, search_area):
        score = 0
        for i in range(5):
            if col+i == search_area.shape[1]:
                break
            elif search_area[row][col+i] == self.token:
                score += 1

        if score == 5:
            return 1000
        else:
            return score

    def se_search(self, row, col, search_area):
        score = 0
        for i in range(5):
            if row+i == search_area.shape[0] or col+i == search_area.shape[1]:
                break
            elif search_area[row+i][col+i] == self.token:
                score += 1

        if score == 5:
            return 1000
        else:
            return score

    def south_search(self, row, col, search_area):
        score = 0
        for i in range(5):
            if row+i == search_area.shape[0]:
                break
            elif search_area[row+i][col] == self.token:
                score += 1

        if score == 5:
            return 1000
        else:
            return score

    def sw_search(self, row, col, search_area):
        score = 0
        for i in range(5):
            if col-i == -1 or row+i == search_area.shape[0]:
                break
            elif search_area[row+i][col-i] == self.token:
                score += 1

        if score == 5:
            return 1000
        else:
            return score

    def west_search(self, row, col, search_area):
        score = 0
        for i in range(5):
            if col-i == -1:
                break
            elif search_area[row][col-i] == self.token:
                score += 1

        if score == 5:
            return 1000
        else:
            return score

    def nw_search(self, row, col, search_area):
        score = 0
        for i in range(5):
            if row-i == -1 or col-i == -1:
                break
            elif search_area[row-i][col-i] == self.token:
                score += 1

        if score == 5:
            return 1000
        else:
            return score


    def evaluate(self, row, col, search_area):
        final_pts = 0
        self.north_score = self.north_search(row,col,search_area)
        self.ne_score = self.ne_search(row,col,search_area)
        self.east_score = self.east_search(row,col,search_area)
        self.se_score = self.se_search(row,col,search_area)
        self.south_score = self.south_search(row,col,search_area)
        self.sw_score = self.sw_search(row,col,search_area)
        self.west_score = self.west_search(row,col,search_area)
        self.nw_score = self.nw_search(row,col,search_area)

        scores = [self.north_score, self.ne_score, self.east_score, self.se_score, self.south_score, self.sw_score, self.west_score, self.nw_score]
        return sum(scores)


"""
Need to improve evaluation function.
Move on to search tree implementation.
"""

