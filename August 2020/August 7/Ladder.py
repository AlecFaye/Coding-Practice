import math

height_angle = input().split()

height = int(height_angle[0])
angle = int(height_angle[1])
angle = angle * math.pi / 180

print(math.ceil(height / math.sin(angle)))
