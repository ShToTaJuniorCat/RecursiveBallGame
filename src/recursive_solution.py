from board import Board
from gui import GUI
from time import sleep
from constants import REFRESH_GUI_TIME

# gui = GUI()
board = Board()
# gui.draw(board.grid)


def solve_game(grid, ball_num):
    # gui.draw(grid)

    sleep(REFRESH_GUI_TIME / 2)

    if Board.is_win(grid):
        return True

    if not Board.has_valid_moves(grid):
        return False

    test_pit = None
    found_pits = 0
    found = False
    for row in grid:
        for pit in row:
            if pit.has_ball:
                if found_pits == ball_num and not found:
                    test_pit = pit
                    found = True
                else:
                    found_pits += 1

    if test_pit is None:
        return False

    # Check if this pit has any neighbour with a ball
    if test_pit.row > 1 and test_pit.col > 1:
        if board.is_possible_move(grid, test_pit, grid[test_pit.row - 2][test_pit.col - 2]):
            grid_copy = Board.copy_grid(grid)
            Board.move_ball_to_pit(grid_copy, grid_copy[test_pit.row][test_pit.col], grid_copy[test_pit.row - 2][test_pit.col - 2])
            # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1")
            # Board.print_grid(grid_copy)
            # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1")
            if solve_game(grid_copy, 0):
                return True
            # gui.draw(grid)
            sleep(REFRESH_GUI_TIME)

    if test_pit.row > 2 and test_pit.col < len(grid[0]) - 2:
        if board.is_possible_move(grid, test_pit, grid[test_pit.row - 2][test_pit.col + 2]):
            grid_copy = Board.copy_grid(grid)
            Board.move_ball_to_pit(grid_copy, grid_copy[test_pit.row][test_pit.col], grid_copy[test_pit.row - 2][test_pit.col + 2])
            # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2")
            # Board.print_grid(grid_copy)
            # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2")
            if solve_game(grid_copy, 0):
                return True
            # gui.draw(grid)
            sleep(REFRESH_GUI_TIME)

    if test_pit.col > 4:
        if board.is_possible_move(grid, test_pit, grid[test_pit.row][test_pit.col - 4]):
            grid_copy = Board.copy_grid(grid)
            Board.move_ball_to_pit(grid_copy, grid_copy[test_pit.row][test_pit.col], grid_copy[test_pit.row][test_pit.col - 4])
            # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~3")
            # Board.print_grid(grid_copy)
            # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~3")
            if solve_game(grid_copy, 0):
                return True
            # gui.draw(grid)
            sleep(REFRESH_GUI_TIME)

    if test_pit.col < len(grid[0]) - 4:
        if board.is_possible_move(grid, test_pit, grid[test_pit.row][test_pit.col + 4]):
            grid_copy = Board.copy_grid(grid)
            Board.move_ball_to_pit(grid_copy, grid_copy[test_pit.row][test_pit.col], grid_copy[test_pit.row][test_pit.col + 4])
            # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~4")
            # Board.print_grid(grid_copy)
            # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~4")
            if solve_game(grid_copy, 0):
                return True
            # gui.draw(grid)
            sleep(REFRESH_GUI_TIME)

    if test_pit.row < len(grid) - 2 and test_pit.col > 1:
        if board.is_possible_move(grid, test_pit, grid[test_pit.row + 2][test_pit.col - 2]):
            grid_copy = Board.copy_grid(grid)
            # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~5")
            # Board.print_grid(grid_copy)
            # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~5")
            Board.move_ball_to_pit(grid_copy, grid_copy[test_pit.row][test_pit.col], grid_copy[test_pit.row + 2][test_pit.col - 2])
            if solve_game(grid_copy, 0):
                return True
            # gui.draw(grid)
            sleep(REFRESH_GUI_TIME)

    if test_pit.row < len(grid) - 2 and test_pit.col < len(grid[0]) - 2:
        if board.is_possible_move(grid, test_pit, grid[test_pit.row + 2][test_pit.col + 2]):
            grid_copy = Board.copy_grid(grid)
            Board.move_ball_to_pit(grid_copy, grid_copy[test_pit.row][test_pit.col], grid_copy[test_pit.row + 2][test_pit.col + 2])
            # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~6")
            # Board.print_grid(grid_copy)
            # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~6")
            if solve_game(grid_copy, 0):
                return True
            # gui.draw(grid)
            sleep(REFRESH_GUI_TIME)

    return solve_game(grid, ball_num+1)


print(solve_game(board.grid, 0))

