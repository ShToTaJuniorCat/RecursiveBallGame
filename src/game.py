from board import Board  # Make sure to adjust the import path if necessary
import pygame


class Game:
    def __init__(self, gui):
        # Initialize game state
        self.is_running = True
        self.gui = gui
        self.is_game_over = False
        self.is_win = False

    def is_over(self, board):
        over = board.is_win(board.grid) or not board.has_valid_moves(board.grid)
        self.is_game_over = over
        self.is_win = board.is_win(board.grid)

        return over

    def handle_events(self, board):
        # Handle user input events (e.g., mouse clicks)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Handle player's move based on the clicked position
                if not self.is_game_over:
                    x, y = pygame.mouse.get_pos()
                    return board.handle_click(x, y)
                else:
                    return True
        else:
            return False

    def reset(self):
        self.is_running = True
        self.is_game_over = False
