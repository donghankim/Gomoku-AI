from config import get_args
import numpy as np
import pygame
from player import Player
from board import Board
import pdb


def main():
    config = get_args()
    board = Board(config)
    p1 = Player(config, 'player 1', 'white')
    p2 = Player(config, 'player 2', 'black')
    curr_player = p1

    pygame.init()
    window = pygame.display.set_mode((1300,1000))
    pygame.display.set_caption("Gomoku AI")
    clock = pygame.time.Clock()
    myfont = pygame.font.SysFont("arial", 45)
    welcome_text = myfont.render("Gomoku", False, (0,0,0))

    # Game loop
    while board.game_run:
        window.fill([255,178,102])
        window.blit(welcome_text, (1000, 50))
        #clock.tick(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                board.game_run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x_pos, y_pos = event.pos
                print(event.pos)
                x_board = abs((x_pos//47) - 1)
                y_board = abs((y_pos//47) - 1)
                print(x_board, y_board)
                if curr_player.valid_move(x_board, y_board, board.board):
                    board.board[x_board][y_board] = curr_player.token
                    if board.check_win(curr_player.token):
                        print(f"{p1.name} wins the game!")
                        board.game_run = False
                    else:
                        if curr_player == p1:
                            curr_player = p2
                        else:
                            curr_player = p1

        board.draw_board(window)
        pygame.display.update()


    pygame.quit()

    print(board.board.T)
    print("Game successfully terminated.")


if __name__ == '__main__':
    main()


"""
Things to do:
1. board finished, but still some issues with edge cases (1 and 18)
2. Create Minimax search
"""
