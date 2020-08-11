def calculate_order(_shape):
    return ""


def calculate_area(_shape):
    return ""


points_count = int(input())

while points_count != 0:
    shape = []

    for count in range(points_count):
        point_input = input().split()
        point = (int(point_input[0]), int(point_input[1]))
        shape.append(point)

    order = calculate_order(shape)
    area = calculate_area(shape)

    points_count = int(input())
