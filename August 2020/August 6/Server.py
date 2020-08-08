tasks_limit = input().split()

tasks_count = int(tasks_limit[0])
limit = int(tasks_limit[1])

tasks = input().split()

completed_tasks = 0

for task in tasks:
    if limit - int(task) >= 0:
        limit -= int(task)
        completed_tasks += 1
    else:
        break

print(completed_tasks)
