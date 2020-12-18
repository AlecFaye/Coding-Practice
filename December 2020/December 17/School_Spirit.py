score_count = int(input())
scores = []

for count in range(score_count):
    scores.append(int(input()))

group_score = 0
for index in range(len(scores)):
    group_score += (1/5) * (scores[index]) * (4/5) ** index
print(round(group_score, 1))

average_score = 0
for x in range(len(scores)):
    for y in range(len(scores)):
        if y < x:
            average_score += (1/5) * (scores[y]) * (4/5) ** y
        elif y > x:
            average_score += (1/5) * (scores[y]) * (4/5) ** (y - 1)
print(round(average_score / len(scores), 13))
