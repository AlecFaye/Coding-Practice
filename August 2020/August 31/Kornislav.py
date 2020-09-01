sides = input().split()
sides = [int(s) for s in sides]

sides.sort()

print(sides[0] * sides[2])
