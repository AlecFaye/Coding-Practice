cases = int(input())

for test in range(cases):
    rotations, phrase = map(str, input().split())
    rotations = int(rotations)

    for x in range(rotations):
        cut_count = len(phrase) // 4
        if cut_count == 0:
            break

        if x % 2 == 1:
            phrase = phrase[:len(phrase) - cut_count]
        else:
            phrase = phrase[cut_count:]

    print(phrase)
