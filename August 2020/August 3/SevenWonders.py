cards = input()

tablet_count = cards.count("T")
compass_count = cards.count("C")
gear_count = cards.count("G")

points = tablet_count ** 2 + compass_count ** 2 + gear_count ** 2

set_exist = False
set_count = tablet_count

if tablet_count > 0 and compass_count > 0 and gear_count > 0:
    set_exist = True

    if set_count > compass_count:
        set_count = compass_count
    if set_count > gear_count:
        set_count = gear_count

if set_exist:
    points += set_count * 7

print(points)
