import math

diameter, volume = map(int, input().split())

while volume != 0:
    print(round(pow((pow(diameter, 3) - 6 * volume / math.pi), 1.0/3), 9))
    diameter, volume = map(int, input().split())
