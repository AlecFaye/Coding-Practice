cases = int(input())

for test in range(cases):
    first = input()
    second = input()

    difference = ""

    for letter in range(len(first)):
        if first[letter] == second[letter]:
            difference += "."
        else:
            difference += "*"

    print(first)
    print(second)
    print(difference)
    print()
