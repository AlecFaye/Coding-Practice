n = int(input())
numbers = []

for digit in range(n):
    numbers.append(input())

for i in range(n - 1, -1, -1):
    print(numbers[i])
