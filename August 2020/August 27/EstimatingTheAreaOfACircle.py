import math

radius, square, circle = map(float, input().split())

while radius != 0:
    true_area = pow(radius, 2) * math.pi

    print(true_area, end=" ")
    print(4.0 * pow(radius, 2) * circle / square)

    radius, square, circle = map(float, input().split())
