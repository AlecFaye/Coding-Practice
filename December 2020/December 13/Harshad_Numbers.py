str_number = input()
digit_sum = 0

for digit in str_number:
    digit_sum += int(digit)

while True:
    if int(str_number) % digit_sum == 0:
        print(str_number)
        break
    else:
        str_number = str(int(str_number) + 1)
        digit_sum = 0
        for digit in str_number:
            digit_sum += int(digit)
