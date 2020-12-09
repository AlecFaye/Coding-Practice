total_teams = int(input())
placed = {""}

for x in range(total_teams):
    institution, team = map(str, input().split())
    if institution not in placed:
        print(institution, team)
        placed.add(institution)
    if len(placed) == 13:
        break
