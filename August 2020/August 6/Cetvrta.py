x_coordinates = {}
y_coordinates = {}

for count in range(3):
    point = input().split()

    if point[0] not in x_coordinates:
        x_coordinates[point[0]] = 1
    else:
        x_coordinates[point[0]] += 1

    if point[1] not in y_coordinates:
        y_coordinates[point[1]] = 1
    else:
        y_coordinates[point[1]] += 1

x_coord = 0
y_coord = 0

for coord in x_coordinates:
    if x_coordinates[coord] == 1:
        x_coord = coord

for coord in y_coordinates:
    if y_coordinates[coord] == 1:
        y_coord = coord

print(x_coord + " " + y_coord)
