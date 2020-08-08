friends_input = input().split()

friend_count = int(friends_input[0])
friendship_count = int(friends_input[1])

money = []

for count in range(friend_count):
    money.append(int(input()))

friendship = []

for count in range(friendship_count):
    ship = input().split()
    friendship.append([int(ship[0]), int(ship[1])])

possible = True

for ship in friendship:
    friend1 = ship[0]
    friend2 = ship[1]

    if money[friend1] < 0 < money[friend2]:
        money[friend1] += money[friend2]
        money[friend2] = 0
    elif money[friend2] < 0 < money[friend1]:
        money[friend2] += money[friend1]
        money[friend1] = 0

friendship.reverse()
for ship in friendship:
    friend1 = ship[0]
    friend2 = ship[1]

    if money[friend1] < 0 < money[friend2]:
        money[friend1] += money[friend2]
        money[friend2] = 0
    elif money[friend2] < 0 < money[friend1]:
        money[friend2] += money[friend1]
        money[friend1] = 0

for x in money:
    if x != 0:
        possible = False

if possible:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
