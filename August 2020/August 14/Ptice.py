questions_count = int(input())
answers = input()

adrian = ["A", "B", "C"]
bruno = ["B", "A", "B", "C"]
goran = ["C", "C", "A", "A", "B", "B"]

correct_answers = [0, 0, 0]

for index in range(len(answers)):
    a_index = index % len(adrian)
    b_index = index % len(bruno)
    c_index = index % len(goran)

    answer = answers[index]

    if answer == adrian[a_index]:
        correct_answers[0] += 1
    if answer == bruno[b_index]:
        correct_answers[1] += 1
    if answer == goran[c_index]:
        correct_answers[2] += 1

max_correct = max(correct_answers)

print(max_correct)
for index in range(len(correct_answers)):
    amount_correct = correct_answers[index]
    if amount_correct == max_correct:
        if index == 0:
            print("Adrian")
        elif index == 1:
            print("Bruno")
        elif index == 2:
            print("Goran")
