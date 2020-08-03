modulo_count = []

for case in range(10):
    number = int(input())

    remainder = divmod(number, 42)[1]

    if remainder not in modulo_count:
        modulo_count.append(remainder)

print(len(modulo_count))
