line = input()

votes = {}

while line != "***":
    if line not in votes:
        votes[line] = 1
    else:
        votes[line] += 1
    line = input()

majority_votes = 0
runners = 1
winner = ""

for name in votes:
    if votes[name] > majority_votes:
        majority_votes = votes[name]
        runners = 1
        winner = name
    elif votes[name] == majority_votes:
        runners += 1

if runners > 1:
    print("Runoff!")
else:
    print(winner)
