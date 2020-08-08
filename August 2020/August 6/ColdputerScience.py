date_count = int(input())

cold_days = 0

days = input().split()

for day in days:
    if int(day) < 0:
        cold_days += 1

print(cold_days)
