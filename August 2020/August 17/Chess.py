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

    # Checks if the move is impossible
    if letter_number[old_position[0]] % 2 != letter_number[new_position[0]] % 2:
        if old_position[1] % 2 == new_position[1] % 2:
            empty_moves.append("Impossible")
            return empty_moves

    elif letter_number[old_position[0]] % 2 == letter_number[new_position[0]] % 2:
        if old_position[1] % 2 != new_position[1] % 2:
            empty_moves.append("Impossible")
            return empty_moves

    # Checks if the move is on the same square
    if letter_number[old_position[0]] == letter_number[new_position[0]] and old_position[1] == new_position[1]:
        empty_moves.append([old_position[0], old_position[1]])
        return empty_moves

    # Determines the moves required to move the piece
    else:
        x_slope = old_position[1] - new_position[1]
        y_slope = letter_number[old_position[0]] - letter_number[new_position[0]]
        if x_slope != 0:
            slope = float(y_slope / x_slope)
        else:
            slope = 0

        # Adds the beginning position
        empty_moves.append([old_position[0], old_position[1]])

        if slope != 1 or slope != -1:
            found = False
            x = letter_number[old_position[0]]
            y = old_position[1]

            # Quadrant 1
            while x < 8 and y < 8 and not found:
                x += 1
                y += 1
                found = determine_slope(empty_moves, x, y)

            x = letter_number[old_position[0]]
            y = old_position[1]

            # Quadrant 2
            while x > 1 and y < 8 and not found:
                x -= 1
                y += 1
                found = determine_slope(empty_moves, x, y)

            x = letter_number[old_position[0]]
            y = old_position[1]

            # Quadrant 3
            while x > 1 and y > 1 and not found:
                x -= 1
                y -= 1
                found = determine_slope(empty_moves, x, y)

            x = letter_number[old_position[0]]
            y = old_position[1]

            # Quadrant 4
            while x < 8 and y > 1 and not found:
                x += 1
                y -= 1
                found = determine_slope(empty_moves, x, y)

        # Adds the last position
        empty_moves.append([new_position[0], new_position[1]])

        return empty_moves


def determine_slope(empty_moves, x, y):
    x_slope = letter_number[new_position[0]] - x
    y_slope = new_position[1] - y

    if x_slope != 0:
        slope = float(y_slope / x_slope)
    else:
        slope = 0

    if slope == 1 or slope == -1:
        for key, value in letter_number.items():
            if value == x:
                empty_moves.append([key, y])
        return True
    return False


for test in range(cases):
    positions = input().split()

    old_position = (positions[0], int(positions[1]))
    new_position = (positions[2], int(positions[3]))

    moves = get_moves()

    for index in range(len(moves)):
        current_move = moves[index]

        # Prints impossible if the move is not possible
        if current_move == "Impossible":
            print(current_move)

        # Prints the moves if possible
        else:
            if index == 0:
                print(len(moves) - 1, end=" ")
            for position in current_move:
                print(position, end=" ")

    if moves[0] != "Impossible":
        print()
