empty, found, cost = map(int, input().split())

drinks = 0

while (empty + found) >= cost:
    bought = (empty + found) // cost
    empty = bought + (empty + found) % cost
    found = 0
    drinks += bought

print(int(drinks))
