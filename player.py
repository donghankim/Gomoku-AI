import pdb

class Player(object):
    def __init__(self, config, name, token):
        self.config = config
        self.name = name

        if token == 'white':
            self.color = (255,255,255)
            self.token = 1
        else:
            self.color = (0,0,0)
            self.token = 2

        self.history = []
        self.win = False


    def valid_move(self,x,y,board):
        if x > self.config.cols-1 or y > self.config.rows-1:
            print("Move out of bounds.")
            return False
        elif x < 0 or y < 0:
            print("Move out of bounds.")
            return False
        elif board[x][y] != 0:
            print("There already is a piece!")
            return False
        else:
            self.history.append((x, y))
            return True

    # check for 3-3 rule (do this last)
    def check_33(self, token):
        pass

    def evaluate(self, board):
        pass













