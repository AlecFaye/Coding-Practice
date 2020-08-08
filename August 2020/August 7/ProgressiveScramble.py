symbols = {
    " ": 0,
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26
}


def first_encryption(_phrase):
    new_phrase = []

    if action == "e":
        for character in _phrase:
            new_phrase.append(symbols[character])
    elif action == "d":
        for character in _phrase:
            for key, value in symbols.items():
                if character == value:
                    new_phrase.append(key)

    return new_phrase


def second_encryption(_phrase):
    if action == "e":
        for index in range(len(_phrase)):
            if index != 0:
                _phrase.insert(index, _phrase[index] + _phrase[index - 1])
                _phrase.pop(index + 1)
    elif action == "d":
        for index in range(len(_phrase) - 1, -1, -1):
            if index != 0:
                _phrase.insert(index, _phrase[index] - _phrase[index - 1])
                _phrase.pop(index + 1)

    return _phrase


def third_encryption(_phrase):
    if action == "e":
        for index in range(len(_phrase)):
            character = _phrase[index]
            modulo = divmod(int(character), 27)[1]
            _phrase.insert(index, modulo)
            _phrase.pop(index + 1)
    elif action == "d":
        for index in range(len(_phrase)):
            if index != 0:
                character = int(_phrase[index])
                while character < int(_phrase[index - 1]):
                    character += 27
                _phrase.insert(index, character)
                _phrase.pop(index + 1)

    return _phrase


def fourth_encryption(_phrase):
    new_phrase = []

    if action == "e":
        for character in _phrase:
            for key, value in symbols.items():
                if character == value:
                    new_phrase.append(key)
    elif action == "d":
        for character in _phrase:
            new_phrase.append(symbols[character])

    return new_phrase


cases = int(input())

for test in range(cases):
    case = input()
    action = case[0]
    phrase = case[2:]

    if action == "e":
        first_phrase = first_encryption(phrase)
        second_phrase = second_encryption(first_phrase)
        third_phrase = third_encryption(second_phrase)
        fourth_phrase = fourth_encryption(third_phrase)

        for char in fourth_phrase:
            print(char, end="")
        print()
    elif action == "d":
        first_phrase = fourth_encryption(phrase)
        second_phrase = third_encryption(first_phrase)
        third_phrase = second_encryption(second_phrase)
        fourth_phrase = first_encryption(third_phrase)

        for char in fourth_phrase:
            print(char, end="")
        print()
