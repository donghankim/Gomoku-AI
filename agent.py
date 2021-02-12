from player import Player
import numpy as np
import random
from copy import deepcopy
import pdb


class Naiive(Player):
    def __init__(self, config, name, token):
        super().__init__(config, name, token)

    def make_move(self, wait_player, board):
        recent_x = wait_player.history[-1][0]
        recent_y = wait_player.history[-1][0]

        while True:
            random_x = random.randint(recent_x-1, recent_x+1)
            random_y = random.randint(recent_y-1, recent_y+1)
            if self.valid_move(random_x, random_y, board.board):
                break
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


    def make_move(self, wait_player, board):
        recent_x = wait_player.history[-1][0]
        recent_y = wait_player.history[-1][1]
        x_min = recent_x - 5
        x_max = recent_x + 5
        y_min = recent_y - 5
        y_max = recent_y + 5

        # finding search area grid
        if x_min < 0:
            x_min = 0
        elif x_max > 18:
            x_max = 18
        elif y_min < 0:
            y_min = 0
        elif y_max > 18:
            y_max = 18

        search_area = board.board[range(y_min, y_max),:]
        search_area = search_area[:,range(x_min, x_max)]
        states = deepcopy(search_area)

        # it should not search where there already is a piece -> fix this
        for i in search_area[0]:
            for j in search_area[1]:
                states[i][j] = self.evaluate(i, j, search_area)

        # print(states)
        max_idx = np.unravel_index(states.argmax(), states.shape)
        x_move = max_idx[0]
        y_move = max_idx[1]

        while True:
            if self.valid_move(x_move, y_move, board.board):
                break
            else:
                x_move += 1

        return x_move, y_move


    def north_search(self, x, y, search_area):
        score = 0
        for i in range(5):
            if y-i == -1:
                break
            elif search_area[x][y-i] == self.token:
                self.north_score += 1
            elif search_area[x][y-i] == 0 or search_area[x][y-i] == self.op_token:
                continue

        if score == 5:
            return 1000
        else:
            return score

    def ne_search(self, x, y, search_area):
        score = 0
        for i in range(5):
            if x+i == 19 or y-i == -1:
                break
            elif search_area[x+i][y-i] == self.token:
                score += 1
            elif search_area[x+i][y-i] == 0 or search_area[x+i][y-i] == self.op_token:
                continue

        if score == 5:
            return 1000
        else:
            return score

    def east_search(self, x, y, search_area):
        score = 0
        for i in range(5):
            if x+i == 19:
                break
            elif search_area[x+i][y] == self.token:
                score += 1
            elif search_area[x+i][y] == 0 or search_area[x+i][y] == self.op_token:
                continue

        if score == 5:
            return 1000
        else:
            return score

    def se_search(self, x, y, search_area):
        score = 0
        for i in range(5):
            if x+i == 19 or y+i == 19:
                break
            elif search_area[x+i][y+i] == self.token:
                score += 1
            elif search_area[x+i][y+i] == 0 or search_area[x+i][y+i] == self.op_token:
                continue

        if score == 5:
            return 1000
        else:
            return score

    def south_search(self, x, y, search_area):
        score = 0
        for i in range(5):
            if y+i == 19:
                break
            elif search_area[x][y+i] == self.token:
                score += 1
            elif search_area[x][y+i] == 0 or search_area[x][y+i] == self.op_token:
                continue

        if score == 5:
            return 1000
        else:
            return score

    def sw_search(self, x, y, search_area):
        score = 0
        for i in range(5):
            if x-i == -1 or y+i == 19:
                break
            elif search_area[x-i][y+i] == self.token:
                score += 1
            elif search_area[x-i][y+i] == 0 or search_area[x-i][y+i] == self.op_token:
                continue

        if score == 5:
            return 1000
        else:
            return score

    def west_search(self, x, y, search_area):
        score = 0
        for i in range(5):
            if x-i == -1:
                break
            elif search_area[x-i][y] == self.token:
                score += 1
            elif search_area[x-i][y] == 0 or search_area[x-i][y] == self.op_token:
                continue

        if score == 5:
            return 1000
        else:
            return score

    def nw_search(self, x, y, search_area):
        score = 0
        for i in range(5):
            if x-i == -1 or y-i == -1:
                break
            elif search_area[x-i][y-i] == self.token:
                score += 1
            elif search_area[x-i][y-i] == 0 or search_area[x-i][y-i] == self.op_token:
                continue

        if score == 5:
            return 1000
        else:
            return score


    def evaluate(self, x, y, search_area):
        final_pts = 0
        self.north_score = self.north_search(x,y,search_area)
        self.ne_score = self.ne_search(x,y,search_area)
        self.east_score = self.east_search(x,y,search_area)
        self.se_score = self.se_search(x,y,search_area)
        self.south_score = self.south_search(x,y,search_area)
        self.sw_score = self.sw_search(x,y,search_area)
        self.west_score = self.west_search(x,y,search_area)
        self.nw_score = self.nw_search(x,y,search_area)

        scores = [self.north_score, self.ne_score, self.east_score, self.se_score, self.south_score, self.sw_score, self.west_score, self.nw_score]


        for i in range(len(scores)):
            if scores[i] == 1000:
                final_pts = 1000
                break
            else:
                final_pts += (i+1)*scores[i]

        return final_pts


"""
Update evaluate function -> just take the average maybe?
figure out a way to incooperate the search grid and states array.
"""

