cases = int(input())

for test in range(cases):
    maximum_turns = int(input())
    row_col = input().split()
    row = int(row_col[0])
    col = int(row_col[1])

    end_curb = input()
    end_curb = [curb for curb in end_curb]
    roads = []

    for row_count in range(row):
        road = input()
        road_array = []
        for road_count in range(len(road)):
            road_array.append(road[road_count])
        roads.append(road_array)

    beginning_curb = input()
    beginning_curb = [curb for curb in beginning_curb]
