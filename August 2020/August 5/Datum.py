day_month = input().split()

day = int(day_month[0])
month = int(day_month[1])

weekdays = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]

total_days = day

for current_month in range(1, month):
    if 1 <= current_month <= 7:
        if current_month % 2 == 1:
            total_days += 31
        elif current_month == 2:
            total_days += 28
        else:
            total_days += 30
    else:
        if current_month % 2 == 1:
            total_days += 30
        else:
            total_days += 31

current_weekday = total_days % 7 - 1

print(weekdays[current_weekday])
