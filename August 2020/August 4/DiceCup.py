dice = input().split()
first_die = int(dice[0])
second_die = int(dice[1])

start = 1
dice_sums = {}

for first_roll in range(1, first_die + 1):
    for second_roll in range(1, second_die + 1):
        calculate_sum = first_roll + second_roll

        if calculate_sum not in dice_sums:
            dice_sums[calculate_sum] = 1
        else:
            dice_sums[calculate_sum] += 1

highest_probability = 0
highest_value = 0

sum_values = []

for rolled_sum in dice_sums:
    if dice_sums[rolled_sum] == highest_probability:
        sum_values.append(rolled_sum)
    elif dice_sums[rolled_sum] > highest_probability:
        sum_values.clear()
        sum_values.append(rolled_sum)
        highest_probability = dice_sums[rolled_sum]

for value in sum_values:
    print(value)
