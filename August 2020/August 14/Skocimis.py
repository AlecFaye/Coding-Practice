first, second, third = map(int, input().split())

largest_difference = second - first
if third - second > largest_difference:
    largest_difference = third - second

print(largest_difference - 1)
