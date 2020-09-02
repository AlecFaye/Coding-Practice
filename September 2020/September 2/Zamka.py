left_limit = int(input())
right_limit = int(input())
digit_sum = int(input())

minimal = right_limit + 1
maximal = left_limit - 1

for number in range(left_limit, right_limit + 1):
    letter = str(number)
    total_sum = 0

    for digit in letter:
        total_sum += int(digit)

    if total_sum == digit_sum:
        if number < minimal:
            minimal = number
        if number > maximal:
            maximal = number

print(minimal)
print(maximal)
