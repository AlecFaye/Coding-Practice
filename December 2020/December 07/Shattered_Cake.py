width = int(input())
pieces = int(input())

area = 0

for x in range(pieces):
    dimensions = list(map(int, input().split()))
    area += dimensions[0] * dimensions[1]

print(int(area / width))
