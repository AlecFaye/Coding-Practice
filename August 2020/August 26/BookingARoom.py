room_count, booked_rooms = map(int, input().split())

rooms = {i for i in range(1, room_count + 1)}

for index in range(booked_rooms):
    rooms.remove(int(input()))

if rooms:
    print(rooms.pop())
else:
    print("too late")
