cases = int(input())


def add():
    if a + b == c:
        return True
    return False


def subtract():
    if a - b == c:
        return True
    if b - a == c:
        return True
    return False


def multiply():
    if a * b == c:
        return True
    return False


def divide():
    if a / b == c:
        return True
    if b / a == c:
        return True
    return False


for test in range(cases):
    a, b, c = map(int, input().split())

    possible = add()

    if not possible:
        possible = subtract()

    if not possible:
        possible = multiply()

    if not possible:
        possible = divide()

    if possible:
        print("Possible")
    else:
        print("Impossible")
