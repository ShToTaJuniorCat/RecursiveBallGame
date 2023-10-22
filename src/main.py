import pygame
from game import Game
from gui import GUI
from board import Board


# Initialize Pygame
pygame.init()

# Create a Game instance
gui = GUI()
game = Game(gui)


def start_game():
    board = Board()
    gui.draw(board.grid)

    # Main game loop
    while not game.is_over(board) and game.is_running:
        if game.handle_events(board):
            gui.draw(board.grid)

    gui.display_winning_text(game.is_win)

    while game.is_running and not game.handle_events(board):
        pass

    if game.is_running:
        game.reset()


if __name__ == "__main__":
    while game.is_running:
        start_game()
