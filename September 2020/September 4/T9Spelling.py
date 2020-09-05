cases = int(input())

letter_converter = {
    "a": "2",
    "b": "22",
    "c": "222",
    "d": "3",
    "e": "33",
    "f": "333",
    "g": "4",
    "h": "44",
    "i": "444",
    "j": "5",
    "k": "55",
    "l": "555",
    "m": "6",
    "n": "66",
    "o": "666",
    "p": "7",
    "q": "77",
    "r": "777",
    "s": "7777",
    "t": "8",
    "u": "88",
    "v": "888",
    "w": "9",
    "x": "99",
    "y": "999",
    "z": "9999",
    " ": "0"
}

for test in range(cases):
    message = input()
    digits = ""

    for letter in message:
        if digits == "":
            digits += letter_converter[letter]
        else:
            if digits[-1] == letter_converter[letter][0]:
                digits += " "
            digits += letter_converter[letter]

    print("Case #" + str(test + 1) + ": " + digits)
