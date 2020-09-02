cases = int(input())

for test in range(cases):
    instruction = input().split()

    if instruction[0] == "Simon" and instruction[1] == "says":
        for index in range(2, len(instruction) - 1):
            print(instruction[index], end=" ")
        print(instruction[-1])
