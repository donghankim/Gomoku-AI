# computer/AI class
import copy
from sys import maxsize
import pdb

class Computer(object):
    def __init__(self, name, token, board):
        self.name = name
        self.board = board
        self.scores = []
        self.depth = 0
        self.search_area = 1
        self.possible_moves = []

        if token == 'white':
            self.token = 1
            self.tokenOP = 2
            self.turn = False
        else:
            self.token = 2
            self.tokenOP = 1
            self.turn = True

        self.in_row = None
        self.in_col = None
        self.win = False


    # get AI's move
    def get_move(self):
        self.in_row, self.in_col = self.get_best_move(self.board.board)
        self.possible_moves = []

        if self.board.valid_move(self.in_row, self.in_col, self.token):
            self.board.board[self.in_row][self.in_col] = self.token
            print(f"{self.name} places stone at {self.in_row},{self.in_col}")

            if self.board.check_win(self.board.board, self.token):
                self.win = True

            return self.board.board

        else:
            print(self.board.board)
            self.get_move()


    # Initiate minimax algorithm
    def get_best_move(self, cur_pos):

        pos_positions = self.get_branches(cur_pos, self.token, True)

        for position in pos_positions:
            self.scores.append(self.minimax_eval(position, self.depth, True, -1*maxsize, maxsize))

        best_index = self.scores.index(max(self.scores))
        self.scores = []

        return self.possible_moves[best_index]


    # finding the max value for current position using alpha/beta pruning
    def minimax_eval(self, cur_pos, depth, max_player, alpha, beta):

        if max_player:
            token_check = self.token
        else:
            token_check = self.tokenOP

        # recursion base check
        if self.board.check_win(cur_pos, token_check):
            self.win = True
            return self.board.eval(cur_pos, self)

        elif depth == 0:
            return self.board.eval(cur_pos, self)

        if max_player:
            branches = self.get_branches(cur_pos,token_check, False)
            best = -1*maxsize
            for child in branches:
                eval_ret = self.minimax_eval(child, depth-1, False, alpha, beta)
                best = max(best, eval_ret)
                alpha = max(alpha, eval_ret)
                if beta <= alpha:
                    break

        else:
            branches = self.get_branches(cur_pos, token_check, False)
            best = maxsize
            for child in branches:
                eval_ret = self.minimax_eval(child, depth-1, True, alpha, beta)
                best = min(best, eval_ret)
                beta = min(beta, eval_ret)
                if beta <= alpha:
                    break

        return best


    # get branches near most recent playe
    def get_branches(self, cur_pos, token_check, flag):
        branches = []
        row_minRange = self.board.last_row - self.search_area
        row_maxRange = self.board.last_row + self.search_area
        col_minRange = self.board.last_col - self.search_area
        col_maxRange = self.board.last_col + self.search_area

        if row_minRange < 0:
            row_minRange = 0

        if row_maxRange > self.board.size -1:
            row_maxRange = self.board.size -1

        if col_minRange < 0:
            col_minRange = 0

        if col_maxRange > self.board.size -1:
            col_maxRange = self.board.size -1

        for row in range(row_minRange, row_maxRange+1):
            for col in range(col_minRange, col_maxRange+1):
                if cur_pos[row][col] == 0:
                    branches.append(copy.deepcopy(cur_pos))
                    branches[-1][row][col] = token_check
                    if flag == True:
                        self.possible_moves.append((row, col))

        return branches


