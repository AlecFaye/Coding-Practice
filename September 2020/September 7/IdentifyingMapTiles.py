quad_key = input()
zoom_level = len(quad_key)

x, y = 0, 0

for level in range(zoom_level):
    x *= 2
    y *= 2

    if quad_key[level] == "1":
        x += 1
    elif quad_key[level] == "2":
        y += 1
    elif quad_key[level] == "3":
        x += 1
        y += 1

print(zoom_level, x, y)
