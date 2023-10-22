from constants import *
from pit import Pit
from copy import deepcopy


class Board:
    def __init__(self):
        # Initialize the game board with pits and balls
        self.grid = self.initialize_board()
        self.picked_pit: Pit = None

    @staticmethod
    def initialize_board():
        # Create and populate the game board based on the provided pattern
        grid = []
        for row, row_pattern in enumerate(PATTERN):
            grid_row = []
            for col, char in enumerate(row_pattern):
                """
                Key:
                 =: Placeholder pit. This pit doesn't show and is for programming easiness only.
                 0: Normal pit without a ball.
                 1: Normal pit with a ball.
                 X: Middle pit without a ball.
                 O: Middle pit with a ball.
                """

                if char == '=':
                    pit_color = PLACEHOLDER_PIT_COLOR
                    has_ball = False
                    is_placeholder = True
                    is_middle = False
                elif char == '0':
                    pit_color = PIT_COLOR
                    has_ball = False
                    is_placeholder = False
                    is_middle = False
                elif char == '1':
                    pit_color = PIT_COLOR
                    has_ball = True
                    is_placeholder = False
                    is_middle = False
                elif char == 'X':
                    pit_color = MIDDLE_PIT_COLOR
                    has_ball = False
                    is_placeholder = False
                    is_middle = True
                elif char == 'O':
                    pit_color = MIDDLE_PIT_COLOR
                    has_ball = True
                    is_placeholder = False
                    is_middle = True

                grid_row.append(Pit(row, col, pit_color, has_ball, is_placeholder, is_middle))
            grid.append(grid_row)

        return grid

    @staticmethod
    def print_grid(grid):
        for row in grid:
            for col in row:
                print(str(col), end="")

            print()

        print("\n\n")

    @staticmethod
    def copy_grid(grid):
        grid_copy = []
        for row in grid:
            current_row = []
            for col in row:
                col_copy = deepcopy(col)
                current_row.append(col_copy)

            grid_copy.append(current_row)

        return grid_copy

    @staticmethod
    def is_win(grid):
        for row in grid:
            for pit in row:
                if not pit.is_middle and pit.has_ball:
                    # If there is a non-middle pit with a ball, the game is not over.
                    return False
                elif pit.is_middle and not pit.has_ball:
                    # If there is a middle pit with no ball, the game is not over.
                    return False

        return True

    @staticmethod
    def has_valid_moves(grid):
        """
        Yes, this is a horrible, horrible function.
        No, I don't give a flying fuck about performance.
        You are welcome to improve it if you feel like it.
        """

        # Check if there are valid moves left
        for row in grid:
            for pit in row:
                if pit.has_ball:
                    # Check if this pit has any neighbour with a ball
                    if pit.row > 1 and pit.col > 1:
                        if Board.is_possible_move(grid, pit, grid[pit.row - 2][pit.col - 2]):
                            return True

                    if pit.row > 2 and pit.col < len(grid[0]) - 2:
                        if Board.is_possible_move(grid, pit, grid[pit.row - 2][pit.col + 2]):
                            return True

                    if pit.col > 4:
                        if Board.is_possible_move(grid, pit, grid[pit.row][pit.col - 4]):
                            return True

                    if pit.col < len(grid[0]) - 4:
                        if Board.is_possible_move(grid, pit, grid[pit.row][pit.col + 4]):
                            return True

                    if pit.row < len(grid) - 2 and pit.col > 1:
                        if Board.is_possible_move(grid, pit, grid[pit.row + 2][pit.col - 2]):
                            return True

                    if pit.row < len(grid) - 2 and pit.col < len(grid[0]) - 2:
                        if Board.is_possible_move(grid, pit, grid[pit.row + 2][pit.col + 2]):
                            return True

        return False

    def handle_click(self, x, y):
        # Handle player's click on the board
        row = round((y - GRID_SIZE) / (25 + GRID_SIZE + GRID_SPACING))
        col = round((x - GRID_SIZE) / (GRID_SIZE + GRID_SPACING))
        pit = self.grid[row][col]

        if pit.is_placeholder or (not pit.has_ball and self.picked_pit is None):
            return False

        if not pit.has_ball and self.picked_pit is not None:
            return self.can_move_picked_ball(pit)

        return self.pick_ball_from_pit(pit)

    def pick_ball_from_pit(self, pit):
        # Check if the picked pit is already picked
        if pit is self.picked_pit:  # If so, drop the ball in that pit and return True (indicating a change occurred)
            self.drop_current_ball()
            self.picked_pit = None
            return True

        # Check if there is already a picked pit
        if self.picked_pit is not None:
            self.drop_current_ball()  # If so, drop the ball in that pit

        pit.pick_ball()  # Pick ball from pit
        self.picked_pit = pit  # Set current picked pit to be that pit
        return True  # Indicating a change occurred

    def drop_current_ball(self):
        self.picked_pit.drop_ball()

    @staticmethod
    def is_possible_move(grid, original_pit, target_pit):
        # Check if the target pit already has a ball or is placeholder
        if target_pit.is_placeholder or target_pit.has_ball or not original_pit.has_ball:
            return False

        # Calculate the absolute differences in rows and columns between the target pit and the selected pit
        row_diff = abs(target_pit.row - original_pit.row)
        col_diff = abs(target_pit.col - original_pit.col)

        # Check if both row and column differences are even and their sum is 4
        if not (row_diff % 2 == 0 and col_diff % 2 == 0 and row_diff + col_diff == 4):
            return False

        # Calculate the average row and column positions between the target pit and the selected pit
        row_avg = int((target_pit.row + original_pit.row) / 2)
        col_avg = int((target_pit.col + original_pit.col) / 2)

        # Check if the pit at the calculated average position contains a ball
        if not grid[row_avg][col_avg].has_ball:
            return False

        # If all conditions are met, return True to indicate that the ball can be moved to the target pit
        return True

    def can_move_picked_ball(self, target_pit):
        # Check if the target pit already has a ball
        if target_pit.has_ball:
            return False

        # Calculate the absolute differences in rows and columns between the target pit and the selected pit
        row_diff = abs(target_pit.row - self.picked_pit.row)
        col_diff = abs(target_pit.col - self.picked_pit.col)

        # Check if both row and column differences are even and their sum is 4
        if not (row_diff % 2 == 0 and col_diff % 2 == 0 and row_diff + col_diff == 4):
            return False

        # Calculate the average row and column positions between the target pit and the selected pit
        row_avg = int((target_pit.row + self.picked_pit.row) / 2)
        col_avg = int((target_pit.col + self.picked_pit.col) / 2)

        # Check if the pit at the calculated average position contains a ball
        if not self.grid[row_avg][col_avg].has_ball:
            return False

        # If all conditions are met, move the ball as requested
        return self.move_picked_ball_to_pit(target_pit, self.grid[row_avg][col_avg])

    def move_picked_ball_to_pit(self, pit, middle_pit):
        self.picked_pit.remove_ball()
        self.picked_pit = None
        pit.add_ball()
        middle_pit.remove_ball()
        return True

    @staticmethod
    def move_ball_to_pit(grid, original_pit, target_pit):
        row_avg = int((target_pit.row + original_pit.row) / 2)
        col_avg = int((target_pit.col + original_pit.col) / 2)

        original_pit.remove_ball()
        target_pit.add_ball()
        grid[row_avg][col_avg].remove_ball()

        return True
