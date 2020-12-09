x = int(input())
days = list(map(int, input().split()))

min_debris = days[0]
launch_day = 0

for index in range(len(days)):
    if days[index] < min_debris:
        min_debris = days[index]
        launch_day = index

print(launch_day)
