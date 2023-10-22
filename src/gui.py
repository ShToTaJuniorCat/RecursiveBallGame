import pygame
from constants import *


class GUI:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Hexagonal Ball Game")

    def draw(self, grid):
        # Draw the game board and UI elements
        self.screen.fill((255, 255, 255))  # Clear the screen
        self.draw_grid(grid)  # Draw the game board
        pygame.display.flip()  # Update the display

    def draw_pit(self, pit):
        if pit.color:
            pygame.draw.circle(surface=self.screen,
                               color=pit.color,
                               center=self.get_pit_position(pit.row, pit.col),
                               radius=GRID_SIZE // 2)

        if pit.has_ball:
            pygame.draw.circle(surface=self.screen,
                               color=pit.ball_color,
                               center=self.get_pit_position(pit.row, pit.col),
                               radius=GRID_SIZE // 2.5)

    def draw_grid(self, grid):
        # Draw the board, balls, and UI elements
        for row_index, row in enumerate(grid):
            for col_index, col in enumerate(row):
                pit = grid[row_index][col_index]
                self.draw_pit(pit)

    @staticmethod
    def get_pit_position(row, col):
        # Calculate the position to draw a ball based on row and column
        x = col * (GRID_SIZE + GRID_SPACING) + GRID_SIZE
        y = 25 * row + (row * (GRID_SIZE + GRID_SPACING) + GRID_SIZE)
        return x, y

    def display_winning_text(self, is_win):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(ENDGAME_TEXT[is_win], True, ENDGAME_TEXT_COLOR)
        text_rect = text.get_rect()
        text_rect.center = (ENDGAME_TEXT_X // 2, ENDGAME_TEXT_Y // 2)
        self.screen.blit(text, text_rect)
        pygame.display.flip()
