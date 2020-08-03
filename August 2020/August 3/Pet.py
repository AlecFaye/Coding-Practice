winner = 0
highest_score = 0

for contestant in range(5):
    scores = input().split()
    score = 0

    for point in scores:
        score += int(point)

    if score > highest_score:
        winner = contestant + 1
        highest_score = score

print(str(winner) + " " + str(highest_score))
