cases = int(input())

total_minutes = 0
total_seconds = 0

for test in range(cases):
    minutes, seconds = map(int, input().split())
    total_minutes += minutes
    total_seconds += seconds

SL_minute = total_seconds / (total_minutes * 60)

if SL_minute <= 1:
    print("measurement error")
else:
    print(SL_minute)
