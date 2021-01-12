import pdb
class Player(object):
    def __init__(self, name, token):
        self.name = name

        if token == 'white':
            self.token = 1
        else:
            self.token = 2

        self.win = False

    def get_move(self):
        cord = input(f"{self.name} enter coordinate: ").split()
        x, y = int(cord[0]), int(cord[1])
        return (x,y)









