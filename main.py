# Main Gomoku Function
import numpy as np
from player import Player
from board import Board
from computer import Computer
import pdb


def main():
    # Settings
    board = Board()
    p1 = Player('player 1', 'white')
    p2 = Player('player 2', 'black')

    # Game loop
    while board.game_run:
        while not board.set_move(p1, p1.get_move()):
            pass
        if board.check_win(p1.token):
            print(f"{p1.name} wins the game!")
            break
        else:
            while not board.set_move(p2, p2.get_move()):
                pass
            if board.check_win(p2.token):
                print(f"{p2.name} wins the game!")
                break

        print(board.board)
    print(board.board)
    print("Game successfully terminated.")


if __name__ == '__main__':
    main()


