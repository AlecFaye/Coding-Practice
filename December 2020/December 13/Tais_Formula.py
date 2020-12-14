cases = int(input())

area = 0
data = []
point = []

for count in range(cases):
    data_input, point_input = list(map(float, input().split()))
    data.append(data_input / 1000)
    point.append(point_input)

for index in range(1, cases):
    first = (point[index] + point[index - 1]) / 2
    second = data[index] - data[index - 1]
    area += first * second

print(area)
