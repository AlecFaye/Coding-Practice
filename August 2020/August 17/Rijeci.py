count = int(input())

letter_count = {
    "A": 1,
    "B": 0
}

for i in range(count):
    a_letters = letter_count["B"]
    b_letters = letter_count["B"] + letter_count["A"]
    letter_count["A"] = a_letters
    letter_count["B"] = b_letters

print(letter_count["A"], letter_count["B"])
