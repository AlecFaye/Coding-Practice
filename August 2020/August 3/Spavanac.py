time = input()

time_hour = int(time.split()[0])
time_minute = int(time.split()[1])

alarm_hour = 0
alarm_minute = 0


if time_minute < 45:
    if time_hour > 0:
        alarm_hour = time_hour - 1
    else:
        alarm_hour = 23
    alarm_minute = time_minute + 15
else:
    alarm_hour = time_hour
    alarm_minute = time_minute - 45

print(str(alarm_hour) + " " + str(alarm_minute))
