from config import get_args
import numpy as np
import pygame
from player import Player
from board import Board
import pdb


# for quiting application
def terminate():
    pygame.display.quit()
    pygame.quit()
    print("Program successfully terminated.")


# for displaying messages
def blit_message(window, message, kind):
    myfont = pygame.font.SysFont("arial", 50)

    if kind == "welcome":
        text = myfont.render(message, False, (255, 255, 255), (0, 0, 0))
        window.blit(text, (1030, 50))

    elif kind == "win message":
        text = myfont.render(message, False, (255, 255, 255), (0, 0, 0))
        text_rect = text.get_rect()
        x, y = pygame.display.get_surface().get_size()
        text_rect.center = (x//2, y//2)
        window.blit(text, text_rect)

    elif kind == "turn":
        text = myfont.render(message, False, (0, 0, 0))
        window.blit(text, (970, 150))

    elif kind == "system message":
        font = pygame.font.SysFont("arial", 30)
        text = font.render(message, False, (255,255,255))
        window.blit(text, (970, 250))

# to display the board
def basic_window(window, board):
    window.fill([255, 178, 102])
    blit_message(window, "Gomoku", "welcome")
    board.draw_board(window)

def main():
    program_run = True
    config = get_args()
    board = Board(config)
    p1 = Player(config, 'player 1', 'white')
    p2 = Player(config, 'player 2', 'black')
    curr_player = p1

    pygame.init()
    window = pygame.display.set_mode((config.window_x, config.window_y))
    pygame.display.set_caption("Gomoku AI")
    clock = pygame.time.Clock()

    # Game loop
    while board.game_run:
        basic_window(window, board)
        blit_message(window, f"{curr_player.name}'s turn", "turn")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                board.game_run = False
                terminate()
                return

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x_pos, y_pos = event.pos
                x_board = abs(round(x_pos/50) - 1)
                y_board = abs(round(y_pos/50) - 1)
                # print(x_board, y_board)
                # print(board.board)
                if curr_player.valid_move(y_board, x_board, board.board):
                    board.board[y_board][x_board] = curr_player.token
                    if board.check_win(curr_player.token):
                        board.game_run = False
                    else:
                        if curr_player == p1:
                            curr_player = p2
                        else:
                            curr_player = p1

        pygame.display.update()

    # Game terminated
    while program_run:
        basic_window(window, board)
        blit_message(window, f"{curr_player.name} wins!", "win message")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                program_run = False
                break

        pygame.display.update()

    terminate()
    return


if __name__ == '__main__':
    main()

