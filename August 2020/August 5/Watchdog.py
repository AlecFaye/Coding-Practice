import math

cases = int(input())


def find_leash_coordinate():
    for x in range(length):
        for y in range(length):
            leash_possibility = True

            if (x, y) not in hatch_coordinates:
                for index in range(len(hatch_coordinates)):
                    hatch = hatch_coordinates[index]
                    distance = math.sqrt((y - hatch[1]) ** 2 + (x - hatch[0]) ** 2)

                    if x - distance < 0 or y - distance < 0 or x + distance > length or y + distance > length:
                        leash_possibility = False

                if leash_possibility:
                    return str(x) + " " + str(y)
    return "poodle"


for test in range(cases):
    side_hatches = input().split()

    length = int(side_hatches[0])
    hatch_count = int(side_hatches[1])

    hatch_coordinates = []

    for count in range(hatch_count):
        coordinate = input().split()
        xy = (int(coordinate[0]), int(coordinate[1]))
        hatch_coordinates.append(xy)

    print(find_leash_coordinate())
