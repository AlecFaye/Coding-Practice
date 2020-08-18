cases = int(input())

letter_number = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8
}


def get_moves():
    empty_moves = []

    if letter_number[old_position[0]] % 2 != letter_number[new_position[0]] % 2:
        if old_position[1] % 2 == new_position[1] % 2:
            empty_moves.append("Impossible")
            return empty_moves

    elif letter_number[old_position[0]] % 2 == letter_number[new_position[0]] % 2:
        if old_position[1] % 2 != new_position[1] % 2:
            empty_moves.append("Impossible")
            return empty_moves

    if letter_number[old_position[0]] == letter_number[new_position[0]] and old_position[1] == new_position[1]:
        empty_moves.append([old_position[0], new_position[1]])
        return empty_moves

    else:
        empty_moves.append("else")
        return empty_moves


for test in range(cases):
    positions = input().split()

    old_position = (positions[0], int(positions[1]))
    new_position = (positions[2], int(positions[3]))

    moves = get_moves()

    for current_move in moves:
        if current_move == "Impossible" or current_move == "else":
            print(current_move)
        else:
            print(len(moves) - 1, end=" ")
            for position in current_move:
                print(position, end=" ")
            print()
