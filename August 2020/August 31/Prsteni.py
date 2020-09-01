ring_count = int(input())

rings = input().split()
rings = [int(r) for r in rings]

first_ring = rings[0]

for index in range(1, len(rings)):
    current_ring = rings[index]
    largest_divisor = 0

    for div in range(current_ring, 0, -1):
        if first_ring % div == 0 and current_ring % div == 0:
            largest_divisor = div
            break

    print(str(first_ring // largest_divisor) + "/" + str(current_ring // largest_divisor))
