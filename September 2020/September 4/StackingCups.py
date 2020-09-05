cases = int(input())

radius = ["Empty"] * 1000

for test in range(cases):
    first, second = map(str, input().split())

    if first.isdigit():
        radius[int(first) // 2] = second
    else:
        radius[int(second)] = first

for colour in radius:
    if colour != "Empty":
        print(colour)
