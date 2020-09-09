conversion = 1000 * (5280 / 4854)

miles = float(input())
paces = conversion * miles

print(int(round(paces, 0)))
