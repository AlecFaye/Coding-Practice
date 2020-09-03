row, col = map(int, input().split())

park_map = []
building = "#"
car = "X"
empty = "."

squashed_cars = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0
}

for x in range(row):
    row_input = input()
    park_row = []

    for y in range(col):
        park_row.append(row_input[y])

    park_map.append(park_row)

for x in range(row - 1):
    for y in range(col - 1):
        able_to_park = True
        crushed_cars = 0

        # Checks if the truck is able to park here
        for check_x in range(2):
            for check_y in range(2):
                if park_map[x + check_x][y + check_y] == "#":
                    able_to_park = False

        # If able to park, count the squashed cars in the parking spot
        if able_to_park:
            for park_x in range(2):
                for park_y in range(2):
                    if park_map[x + park_x][y + park_y] == "X":
                        crushed_cars += 1
            squashed_cars[crushed_cars] += 1

for cars in range(5):
    print(squashed_cars[cars])
