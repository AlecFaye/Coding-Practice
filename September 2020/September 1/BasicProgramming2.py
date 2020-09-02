def one(_digits):
    for x in range(count):
        for y in range(count):
            if x != y:
                if _digits[x] + _digits[y] == 7777:
                    return "Yes"
    return "No"


def two(_digits):
    duplicates = {}

    for digit in digits:
        if digit not in duplicates:
            duplicates[digit] = 1
        else:
            return "Contains duplicate"

    return "Unique"


def three(_digits):
    for digit in digits:
        if digits.count(digit) > count // 2:
            return digit

    return -1


def four(_digits):
    _digits.sort()

    if count % 2 == 1:
        return _digits[count // 2]
    else:
        return str(_digits[count // 2 - 1]) + " " + str(_digits[count // 2])


def five(_digits):
    _digits.sort()
    phrase = ""

    for digit in _digits:
        if 100 <= digit <= 999:
            phrase += str(digit) + " "

    if phrase[-1] == " ":
        phrase = phrase[:len(phrase) - 1]

    return phrase


count, action = map(int, input().split())
digits = input().split()
digits = [int(d) for d in digits]

if action == 1:
    print(one(digits))
elif action == 2:
    print(two(digits))
elif action == 3:
    print(three(digits))
elif action == 4:
    print(four(digits))
elif action == 5:
    print(five(digits))
