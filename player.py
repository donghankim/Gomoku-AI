import copy
# player(human) class

class Player(object):
    def __init__(self, name, token, board):
        self.name = name
        self.board = board

        if token == 'white':
            self.token = 1
            self.turn = False
        else:
            self.token = 2
            self.turn = True

        self.in_row = None
        self.in_col = None
        self.win = False

    def get_move(self):
        cord = input(f"{self.name} enter coordinate: ")
        # maybe add a try/except statemnt here
        row, col = cord.split()
        self.in_row = int(row)
        self.in_col = int(col)

        if self.board.valid_move(self.in_row, self.in_col, self.token):
            self.board.board[self.in_row][self.in_col] = self.token
            print(f"{self.name} places stone at {self.in_row},{self.in_col}")
            new_board = copy.deepcopy(self.board.board)

            if self.board.check_win(new_board, self.token):
                self.win = True

            return self.board.board
        else:
            print(self.board.board)
            self.get_move()






