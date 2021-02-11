from player import Player
import numpy as np
import random
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

    def make_move(self, wait_player, board):
        recent_x = wait_player.history[-1][0]
        recent_y = wait_player.history[-1][1]
        x_min = recent_x - 5
        x_max = recent_x + 5
        y_min = recent_y - 5
        y_max = recent_y + 5

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

        for i in search_area[0]:
            for j in search_area[1]:
                pts = evaluate(i,j, search_area)

    def evaluate(self, x, y, search_area):
        # left search
        if x < 4:
            pass
        else:
            """
            continue from here...
            """



