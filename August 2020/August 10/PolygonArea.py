def calculate_order(_vertices):
    clockwise_count = 0
    counterclockwise_count = 0

    for i in range(len(_vertices)):
        a_index = i
        b_index = (i + 1) % len(_vertices)
        c_index = (i + 2) % len(_vertices)

        a_point = _vertices[a_index]
        b_point = _vertices[b_index]
        c_point = _vertices[c_index]

        left_determinant = b_point[0] * c_point[1] + a_point[0] * b_point[1] + a_point[1] * c_point[0]
        right_determinant = a_point[1] * b_point[0] + b_point[1] * c_point[0] + a_point[0] * c_point[1]

        determinant = left_determinant - right_determinant

        if determinant < 0:
            clockwise_count += 1
        elif determinant > 0:
            counterclockwise_count += 1

    if clockwise_count >= counterclockwise_count:
        return "CW"
    else:
        return "CCW"


def calculate_area(_vertices):
    psum = 0
    nsum = 0

    for i in range(len(_vertices)):
        sindex = (i + 1) % len(_vertices)
        prod = _vertices[i][0] * _vertices[sindex][1]
        psum += prod

    for i in range(len(_vertices)):
        sindex = (i + 1) % len(_vertices)
        prod = _vertices[sindex][0] * _vertices[i][1]
        nsum += prod

    return abs(1/2 * (psum - nsum))


points_count = int(input())

while points_count != 0:
    vertices = []

    for count in range(points_count):
        point_input = input().split()
        point = (int(point_input[0]), int(point_input[1]))
        vertices.append(point)

    order = calculate_order(vertices)
    area = calculate_area(vertices)

    print(order, round(area, 1))

    points_count = int(input())
