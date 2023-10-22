"""
Key:
 =: Placeholder pit. This pit doesn't show and is for programming easiness only.
 0: Normal pit without a ball.
 1: Normal pit with a ball.
 X: Middle pit without a ball.
 O: Middle pit with a ball.
"""
PATTERN = [
    "=========1=========",
    "========1=1========",
    "=======1=0=1=======",
    "1=1=1=0=0=0=1=0=1=1",
    "=1=0=0=0=0=0=0=0=1=",
    "==1=0=0=1=1=0=0=1==",
    "===1=0=1=X=1=0=0===",
    "==1=0=0=1=1=0=0=1==",
    "=0=0=0=0=0=0=0=0=1=",
    "0=1=1=0=0=0=0=1=0=0",
    "=======1=0=1=======",
    "========1=0========",
    "=========0=========",
]

WIDTH = 1000
HEIGHT = 1000
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

ENDGAME_TEXT = {
    True: "Game over! Well done!",
    False: "Game over! No valid moves left."
}

ENDGAME_TEXT_X = WIDTH
ENDGAME_TEXT_Y = 100
ENDGAME_TEXT_COLOR = (0, 0, 0)

GRID_SIZE = WIDTH / (max(len(PATTERN), len(PATTERN[0])) * 2)
GRID_SPACING = HEIGHT / (max(len(PATTERN), len(PATTERN[0])) * 30)

BALL_COLOR = (100, 0, 255)
PICKED_BALL_COLOR = (255, 0, 85)
PIT_COLOR = (0, 240, 240)
MIDDLE_PIT_COLOR = (255, 100, 100)
PLACEHOLDER_PIT_COLOR = None

REFRESH_GUI_TIME = 0
