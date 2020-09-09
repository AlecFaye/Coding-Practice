stars = int(input())
print(str(stars) + ":")

for count in range(2, stars):
    first = count
    second = count - 1
    total_sum = 0

    while total_sum < stars:
        total_sum += first
        if total_sum < stars:
            total_sum += second

    if total_sum == stars:
        print(str(first) + "," + str(second))

    second = count
    total_sum = 0

    while total_sum < stars:
        total_sum += first
        if total_sum < stars:
            total_sum += first

    if total_sum == stars:
        print(str(first) + "," + str(second))
