n, queries = list(map(int, input().split()))
companies = list(map(int, input().split()))

for count in range(queries):
    query, x, y = list(map(int, input().split()))
    if query == 1:
        companies[x - 1] = y
    elif query == 2:
        print(abs(companies[x - 1] - companies[y - 1]))
