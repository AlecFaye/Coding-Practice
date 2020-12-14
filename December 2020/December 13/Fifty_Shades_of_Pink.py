cases = int(input())

session_count = 0

for x in range(cases):
    session = input().lower()
    for index in range(len(session) - 3):
        if len(session) >= 4:
            if session[index: index + 4] == "rose" or session[index: index + 4] == "pink":
                session_count += 1
                break

if session_count == 0:
    print("I must watch Star Wars with my daughter")
else:
    print(session_count)
