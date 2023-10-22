import gui as gui
from constants import *


class Pit:
    def __init__(self, row, col, color, has_ball, is_placeholder, is_middle):
        self.row = row
        self.col = col
        self.color = color
        self.has_ball = has_ball
        self.is_placeholder = is_placeholder
        self.is_middle = is_middle

        if has_ball:
            self.ball_color = BALL_COLOR
        else:
            self.ball_color = None

    def __str__(self):
        """
        Key:
         =: Placeholder pit. This pit doesn't show and is for programming easiness only.
         0: Normal pit without a ball.
         1: Normal pit with a ball.
         X: Middle pit without a ball.
         O: Middle pit with a ball.
        """
        if self.is_placeholder:
            return "="
        elif not self.is_middle:
            if not self.has_ball:
                return '0'
            else:
                return '1'
        else:
            if not self.has_ball:
                return 'X'
            else:
                return 'O'

    def placeholder_check(func):
        def wrapper(self, *args, **kwargs):
            if self.is_placeholder:
                raise TypeError(f"This pit is a placeholder. Function {func} can't run on a placeholder.")
            return func(self, *args, **kwargs)
        return wrapper

    @placeholder_check
    def remove_ball(self):
        # Remove the ball in this pit
        self.has_ball = False
        gui.draw_pit(self)

    @placeholder_check
    def add_ball(self):
        # Add a ball in this pit
        self.has_ball = True
        gui.draw_pit(self)

    @placeholder_check
    def pick_ball(self):
        if not self.has_ball:
            raise TypeError("Can't pick ball from empty pit")

        self.ball_color = PICKED_BALL_COLOR

    @placeholder_check
    def drop_ball(self):
        if not self.has_ball:
            raise TypeError("Can't drop ball from empty pit")

        self.ball_color = BALL_COLOR

    @placeholder_check
    def remove_ball(self):
        if not self.has_ball:
            raise TypeError("Can't remove ball from empty pit")

        self.has_ball = False
        self.ball_color = None

    @placeholder_check
    def add_ball(self):
        if self.has_ball:
            raise TypeError("Can't add ball to empty pit")

        self.has_ball = True
        self.ball_color = BALL_COLOR


    @placeholder_check
    def is_empty(self):
        return not self.has_ball
