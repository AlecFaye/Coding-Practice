limit_cases = input().split()

limit = int(limit_cases[0])
cases = int(limit_cases[1])

occupied = 0
deny_count = 0

for test in range(cases):
    action_count = input().split()
    action = action_count[0]
    count = int(action_count[1])

    if action == "enter":
        if occupied + count > limit:
            deny_count += 1
        else:
            occupied += count
    else:
        occupied -= count

print(deny_count)
