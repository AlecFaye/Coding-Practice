total_bats = int(input())

bats_input = input().split()
bats = [int(bat) for bat in bats_input]

walks_count = 0
batting_average = 0

for bat in bats:
    if bat == -1:
        walks_count += 1
    else:
        batting_average += bat

print(batting_average / (total_bats - walks_count))
