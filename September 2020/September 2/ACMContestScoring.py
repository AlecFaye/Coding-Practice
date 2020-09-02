question_solved = {}
question_time = {}
penalties = {}
penalty_multiplier = 20

line = input()

while line != "-1":
    line = line.split()
    time = int(line[0])
    question = line[1]
    correct = line[2]

    if question not in question_solved:
        if correct == "right":
            question_solved[question] = True
            question_time[question] = time

        elif correct == "wrong":
            question_solved[question] = False
            penalties[question] = 1
    else:
        if correct == "right":
            if not question_solved[question]:
                question_solved[question] = True
                question_time[question] = time

        elif correct == "wrong":
            if not question_solved[question]:
                penalties[question] += 1

    line = input()

total_solved = 0
for question in question_solved:
    if question_solved[question]:
        total_solved += 1

total_time = 0
for question in question_time:
    if question_solved[question]:
        total_time += question_time[question]

total_penalty = 0
for question in penalties:
    if question_solved[question]:
        total_penalty += penalties[question] * penalty_multiplier

print(total_solved, total_time + total_penalty)
