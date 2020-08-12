def a_move(_position):
    if _position == 1:
        _position = 2
    elif _position == 2:
        _position = 1
    return _position


def b_move(_position):
    if _position == 2:
        _position = 3
    elif _position == 3:
        _position = 2
    return _position


def c_move(_position):
    if _position == 1:
        _position = 3
    elif _position == 3:
        _position = 1
    return _position


moves = input()
ball_position = 1

for move in moves:
    if move == "A":
        ball_position = a_move(ball_position)
    elif move == "B":
        ball_position = b_move(ball_position)
    elif move == "C":
        ball_position = c_move(ball_position)

print(ball_position)
