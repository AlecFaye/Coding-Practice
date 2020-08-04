cost = float(input())
lawns = int(input())

total_cost = 0
total_area = 0

for test in range(lawns):
    dimensions = input().split()
    width = float(dimensions[0])
    length = float(dimensions[1])

    total_area += width * length

total_cost = total_area * cost
print(round(total_cost, 8))
