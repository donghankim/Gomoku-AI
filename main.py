# Main Gomoku Function
import numpy as np
from player import Player
from board import Board
from computer import Computer
import pdb


def main_ai():
    b = Board()
    p1 = Player('player 1', 'black', b)
    ai = Computer('AI', 'white', b)

    b.set_test()

    while b.game_run:
        if b.is_full():
            b.game_run = False
            print("game is a draw...")
            break

        elif p1.turn:
            new_pos = p1.get_move()
            p1.turn = False
            ai.turn = True
            print(new_pos)
            if p1.win == True:
                print(f"{p1.name} wins the game!")
                b.game_run = False
                break

        else:
            new_pos = ai.get_move()
            p1.turn = True
            ai.turn = False
            print(new_pos)
            if ai.win == True:
                print(f"{ai.name} wins the game!")
                b.game_run = False
                break

def main_human():
    b = Board()
    p1 = Player('player 1','black', b)
    p2 = Player('player 2','white', b)
    # ai = Computer('black')

    while b.game_run:
        if b.is_full():
            b.game_run = False
            print("game is a draw...")
            break

        elif p1.turn:
            new_pos = p1.get_move()
            p1.turn = False
            p2.turn = True
            print(new_pos)
            if p1.win == True:
                print(f"{p1.name} wins the game!")
                b.game_run = False
                break

        else:
            new_pos = p2.get_move()
            p2.turn = False
            p1.turn = True
            print(new_pos)
            if p2.win == True:
                print(f"{p2.name} wins the game!")
                b.game_run = False
                break


if __name__ == '__main__':
    # main_human()
    main_ai()
    print("Program Terminate")


