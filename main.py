from config import get_args
import numpy as np
import pygame
from player import Player
from board import Board
import pdb


def main():
    config = get_args()
    board = Board()
    p1 = Player(config, 'player 1', 'white')
    p2 = Player(config, 'player 2', 'black')
    curr_player = p1

    pygame.init()
    window = pygame.display.set_mode((1000,600))
    pygame.display.set_caption("Gomoku AI")
    clock = pygame.time.Clock()
    myfont = pygame.font.SysFont("arial", 45)
    board_img_raw = pygame.image.load('images/new_19_19.png')

    board_img = pygame.transform.scale(board_img_raw, (600,600))
    welcome_text = myfont.render("Gomoku AI", False, (255,255,255))

    # Game loop
    while board.game_run:
        window.blit(board_img, (0, 0))
        window.blit(welcome_text, (700, 50))
        clock.tick(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                board.game_run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x_pos, y_pos = event.pos
                print(event.pos)
                x_board = abs(round((x_pos - 15)/30))
                y_board = abs(round((y_pos - 15)//30))
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

        # draw all tokens
        for i in range(config.rows):
            for j in range(config.cols):
                if board.board[i][j] == 1:
                    x_pos = 15 + j*30
                    y_pos = 15 + i*30
                    pygame.draw.circle(window, (255,255,255), (x_pos, y_pos), 9, 0)
                elif board.board[i][j] == 2:
                    x_pos = 15 + j*30
                    y_pos = 15 + i*30
                    pygame.draw.circle(window, (0,0,0), (x_pos, y_pos), 9, 0)

        pygame.display.update()

    pygame.quit()

    print(board.board)
    print("Game successfully terminated.")


if __name__ == '__main__':
    main()


"""
Some issues with drawing board. Fix that first.


"""
