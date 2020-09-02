def one():
    return 7


def two(_digits):
    if _digits[0] > _digits[1]:
        return "Bigger"
    elif _digits[0] == _digits[1]:
        return "Equal"
    else:
        return "Smaller"


def three(_digits):
    median = [_digits[0], _digits[1], _digits[2]]
    median.sort()
    return median[1]


def four(_digits):
    total_sum = 0

    for digit in _digits:
        total_sum += digit

    return total_sum


def five(_digits):
    total_sum = 0

    for digit in _digits:
        if digit % 2 == 0:
            total_sum += digit

    return total_sum


def six(_digits):
    phrase = ""

    for digit in _digits:
        phrase += chr(97 + digit % 26)

    return phrase


def seven(_digits):
    index = 0
    visited = [False] * count

    while True:
        if index >= count:
            return "Out"

        if visited[index]:
            return "Cyclic"

        if index == count - 1:
            return "Done"

        visited[index] = True
        index = _digits[index]


count, action = map(int, input().split())
digits = input().split()
digits = [int(d) for d in digits]

if action == 1:
    print(one())
elif action == 2:
    print(two(digits))
elif action == 3:
    print(three(digits))
elif action == 4:
    print(four(digits))
elif action == 5:
    print(five(digits))
elif action == 6:
    print(six(digits))
elif action == 7:
    print(seven(digits))
