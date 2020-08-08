valid_set = [1, 1, 2, 2, 2, 8]

current_set = input().split()

difference_set = []

for index in range(len(current_set)):
    difference_piece = valid_set[index] - int(current_set[index])
    difference_set.append(difference_piece)

for index in range(len(difference_set)):
    if index != len(difference_set) - 1:
        print(difference_set[index], end=" ")
    else:
        print(difference_set[index])
