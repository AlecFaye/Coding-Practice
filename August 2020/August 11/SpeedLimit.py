data_count = int(input())

while data_count != -1:
    speed = []
    time = []
    total_miles = 0

    for count in range(data_count):
        speed_time = input().split()
        speed.append(int(speed_time[0]))
        time.append(int(speed_time[1]))

    for index in range(len(speed)):
        if index == 0:
            difference_time = time[index]
        else:
            difference_time = time[index] - time[index - 1]

        total_miles += speed[index] * difference_time

    print(total_miles, "miles")

    data_count = int(input())
