# Board class
import numpy as np
import pdb
import copy

class Board(object):
    def __init__(self):
        self.size = 19
        self.win_count = 5
        self.board = np.array([[0] * self.size] * self.size)
        self.game_run = True

        self.last_row = 10
        self.last_col = 10



    def init_board(self):
        self.board = np.aray([[0] * self.size] * self.size)
        return

    def is_full(self):
        if (self.board == 0).sum() == 0:
            return True


    def valid_move(self, in_row, in_col, token):
        temp_board = copy.deepcopy(self.board)

        if in_row > self.size -1 or in_row < 0:
            print("row value must be between 0 and self.size -1...")
            return False

        if in_col > self.size -1 or in_col < 0:
            print("column value must be between 0 and self.size -1...")
            return False

        if temp_board[in_row][in_col] != 0:
            print(f"There already is a rock at position ({in_row},{in_col})...")
            return False

        # check for 3-3 rule
        temp_board[in_row][in_col] = token
        if self.check_threethree(temp_board, token):
            print("Broke the three three rule")

        self.last_row = in_row
        self.last_col = in_col

        return True


    def check_win(self, board_pos, token):
        if self.check_horizontal(board_pos, token, False) or self.check_vertical(board_pos, token, False) or self.check_diagonal_right(board_pos, token, False) or self.check_diagonal_left(board_pos, token, False):
            return True
        else:
            return False


    def check_horizontal(self, board_pos, token, flag):

        if token == 1:
            tokenOP = 2
        else:
            tokenOP = 1

        # for evaluation function
        open_3 = 0; open_4 = 0; close_3 = 0; close_4 = 0

        for row in range(self.size):
            count = 1; add = 1
            for col in range(self.size):
                if flag == True:
                    if col -1 > -1 and col + 4 < self.size:
                        if board_pos[row][col] == token and board_pos[row][col+1] == token and board_pos[row][col+2] == token and board_pos[row][col+3] == token:
                            if board_pos[row][col-1] == tokenOP and board_pos[row][col+4] == tokenOP:
                                continue
                            elif board_pos[row][col-1] == 0 and board_pos[row][col+4] == 0:
                                open_4 += 1
                            else:
                                close_4 += 1

                        elif board_pos[row][col] == token and board_pos[row][col+1] == token and board_pos[row][col+2] == token:
                            if board_pos[row][col-1] == token or board_pos[row][col+3] == token:
                                continue
                            elif board_pos[row][col-1] == 0 and board_pos[row][col+3] == 0:
                                open_3 += 1
                            else:
                                close_3 += 1

                else:
                    if board_pos[row][col] == token:
                        while count < self.win_count + 1:
                            if count == self.win_count:
                                return True

                            elif col + add > self.size -1:
                                break

                            elif board_pos[row][col+add] == token:
                                count += 1
                                add += 1

                            else:
                                count = 1
                                add = 1
                                break

        if flag == True:
            return open_3, open_4, close_3, close_4
        else:
            return False


    def check_vertical(self, board_pos, token, flag):

        # for evaluation function
        open_3 = 0; open_4 = 0; close_3 = 0; close_4 = 0

        for col in range(self.size):
            count = 1; add = 1
            for row in range(self.size):
                if flag == True:
                    if row -1 > -1 and row + 4 < self.size:
                        if board_pos[row][col] == token and board_pos[row+1][col] == token and board_pos[row+2][col] == token and board_pos[row+3][col] == token:
                            if board_pos[row-1][col] == 0 and board_pos[row+4][col] == 0:
                                open_4 += 1
                            else:
                                close_4 += 1

                        elif board_pos[row][col] == token and board_pos[row+1][col] == token and board_pos[row+2][col] == token:
                            if board_pos[row-1][col] == token or board_pos[row+3][col] == token:
                                continue
                            elif board_pos[row-1][col] == 0 and board_pos[row+3][col] == 0:
                                open_3 += 1
                            else:
                                close_3 += 1

                else:
                    if board_pos[row][col] == token:
                        while count < self.win_count + 1:
                            if count == self.win_count:
                                return True

                            elif row + add > self.size -1:
                                break

                            elif board_pos[row+add][col] == token:
                                count += 1
                                add += 1

                            else:
                                count = 1
                                add = 1
                                break

        if flag == True:
            return open_3, open_4, close_3, close_4
        else:
            return False

    def check_diagonal_right(self, board_pos, token, flag):

        # for evaluation function
        open_3 = 0; open_4 = 0; close_3 = 0; close_4 = 0;

        for row in range(self.size):
            for i in range(self.size):
                if flag == True:
                    if row + i - 1 > -1 and row + i + 4 < self.size:
                        if board_pos[row+i][i] == token and board_pos[row+i+1][i+1] == token and board_pos[row+i+2][i+2] == token and board_pos[row+i+3][i+3] == token:
                            if board_pos[row+i-1][i-1] == 0 and board_pos[row+i+4][i+4] == 0:
                                open_4 += 1
                            else:
                                close_4 += 1

                        elif board_pos[row+i][i] == token and board_pos[row+i+1][i+1] == token and board_pos[row+i+2][i+2] == token:
                            if board_pos[row+i-1][i-1] == token or board_pos[row+i+3][i+3] == token:
                                continue
                            elif board_pos[row+i-1][i-1] == 0 and board_pos[row+i+3][i+3] == 0:
                                open_3 += 1
                            else:
                                close_3 += 1

                else:
                    count = 1; add = 1
                    if row + i > self.size - 1:
                        break
                    elif board_pos[row+i][i] == token:
                        while count < self.win_count + 1:
                            if count == self.win_count:
                                return True

                            elif row + i + add > self.size -1:
                                break

                            elif board_pos[row+i+add][i+add] == token:
                                count += 1
                                add += 1

                            else:
                                count = 1
                                add = 1
                                break


        for col in range(1, self.size):
            for i in range(self.size):
                if flag == True:
                    if col + i - 1 > -1 and col + i + 4 < self.size:
                        if board_pos[i][col+i] == token and board_pos[i+1][col+i+1] == token and board_pos[i+2][col+i+2] == token and board_pos[i+3][col+i+3] == token:
                            if board_pos[i-1][col+i-1] == 0 and board_pos[i+4][col+i+4] == 0:
                                open_4 += 1
                            else:
                                close_4 += 1

                        elif board_pos[i][col+i] == token and board_pos[i+1][col+i+1] == token and board_pos[i+2][col+i+2] == token:
                            if board_pos[i-1][col+i-1] == token or board_pos[i+3][col+i+3] == token:
                                continue
                            elif board_pos[i-1][col+i-1] == 0 and board_pos[i+3][col+i+3] == 0:
                                open_3 += 1
                            else:
                                close_3 += 1

                else:
                    count = 1; add = 1
                    if col + i > self.size - 1:
                        break
                    elif board_pos[i][col+i] == token:
                        while count < self.win_count + 1:
                            if count == self.win_count:
                                return True

                            elif col + i + add > self.size - 1:
                                break

                            elif board_pos[i+add][col+i+add] == token:
                                count += 1
                                add += 1

                            else:
                                count = 1
                                add = 1
                                break


        if flag == True:
            return open_3, open_4, close_3, close_4
        else:
            return False


    def check_diagonal_left(self, board_pos, token, flag):

        # for evaluation function
        open_3 = 0; open_4 = 0; close_3 = 0; close_4 = 0

        for row in range(self.size):
            for i in range(self.size, -1, -1):
                count = 1; add = 1
                if flag == True:
                    if row + add + 4 < self.size and i - add - 4 > -1:
                        if board_pos[row+add][i-add] == token and board_pos[row+add+1][i-add-1] == token and board_pos[row+add+2][i-add-2] == token and board_pos[row+add+3][i-add-3] == token:
                            if board_pos[row+add-1][i-add+1] == 0 and board_pos[row+add+4][i-add-4] == 0:
                                open_4 += 1
                            else:
                                close_4 += 1

                        elif board_pos[row+add][i-add] == token and board_pos[row+add+1][i-add-1] == token and board_pos[row+add+2][i-add-2] == token:
                            if board_pos[row+add-1][i-add+1] == token and board_pos[row+add+3][i-add-3] == token:
                                continue
                            elif board_pos[row+add-1][i-add+1] == 0 and board_pos[row+add+3][i-add-3] == 0:
                                open_3 += 1
                            else:
                                close_3 += 1

                else:
                    if row + add > self.size -1 or i -add < 0:
                        break
                    elif board_pos[row+add][i-add] == token:
                        while count < self.win_count + 1:
                            if count == self.win_count:
                                return True

                            elif row + add > self.size -1 or i - add < 0:
                                break

                            elif board_pos[row+add][i-add] == token:
                                count += 1
                                add += 1

                            else:
                                count = 1
                                add = 1
                                break

        if flag == True:
            return open_3, open_4, close_3, close_4
        else:
            return False


    # checks for 3-3 rule
    def check_threethree(self, board_pos, token):
        prev_count = self.win_count
        self.win_count = 3
        if (self.check_horizontal(board_pos, token, False) and self.check_vertical(board_pos, token, False)) or (self.check_diagonal_left(board_pos, token, False) and self.check_diagonal_right(board_pos, token, False)):
            self.win_count = prev_count
            return True
        else:
            self.win_count = prev_count
            return False

    # heuristic evaluation function
    def eval(self, cur_pos, player):
        # get all the empty squares on the board
        empty_ = (cur_pos == 0).sum()

        if player.token == 1:
            token = 1
            tokenOP = 2
        else:
            token = 2
            tokenOP = 1

        # if player(ai) won the game
        if player.win:
            player.win = False
            return (empty_ + 1000)

        # if all the positions on the board is full, or no winner
        elif self.is_full():
            return 0

        # if neither win or board is full
        else:
            my_val = 0; op_val = 0
            Hopen_3, Hopen_4, Hclose_3, Hclose_4 = self.check_horizontal(cur_pos, token, True)
            Vopen_3, Vopen_4, Vclose_3, Vclose_4 = self.check_vertical(cur_pos, token, True)
            DRopen_3, DRopen_4, DRclose_3, DRclose_4 = self.check_diagonal_right(cur_pos, token, True)
            DLopen_3, DLopen_4, DLclose_3, DLclose_4 = self.check_diagonal_left(cur_pos, token, True)

            my_val = 100*(Hopen_3+Vopen_3+DRopen_3+DLopen_3) + 10*(Hclose_3+Vclose_3+DRclose_3+DLclose_3) + 150*(Hopen_4+Vopen_4+DRopen_4+DLopen_4) + 20*(Hclose_4+Vclose_4+DRclose_4+DLclose_4)

            OPHopen_3, OPHopen_4, OPHclose_3, OPHclose_4 = self.check_horizontal(cur_pos, tokenOP, True)
            OPVopen_3, OPVopen_4, OPVclose_3, OPVclose_4 = self.check_vertical(cur_pos, tokenOP, True)
            OPDRopen_3, OPDRopen_4, OPDRclose_3, OPDRclose_4 = self.check_diagonal_right(cur_pos, tokenOP, True)
            OPDLopen_3, OPDLopen_4, OPDLclose_3, OPDLclose_4 = self.check_diagonal_left(cur_pos, tokenOP, True)

            op_val = 150*(OPHopen_3+OPVopen_3+OPDRopen_3+OPDLopen_3) + 20*(OPHclose_3+OPVclose_3+OPDRclose_3+OPDLclose_3) + 200*(OPHopen_4+OPVopen_4+OPDRopen_4+OPDLopen_4) + 30*(OPHclose_4+OPVclose_4+OPDRclose_4+OPDLclose_4)

            return (my_val-op_val)


    def set_test(self):
        pass
        # self.board[10][10] = 1
        # self.board[10][11] = 1
        # self.board[10][9] = 1

