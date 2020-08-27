gunnar_dice = [int(number) for number in input().split()]
emma_dice = [int(number) for number in input().split()]


def first_attempt():
    gunnar_probability = {}
    emma_probability = {}

    for first in range(gunnar_dice[0], gunnar_dice[1] + 1):
        for second in range(gunnar_dice[2], gunnar_dice[3] + 1):
            if first + second not in gunnar_probability:
                gunnar_probability[first + second] = 1
            else:
                gunnar_probability[first + second] += 1

    for first in range(emma_dice[0], emma_dice[1] + 1):
        for second in range(emma_dice[2], emma_dice[3] + 1):
            if first + second not in emma_probability:
                emma_probability[first + second] = 1
            else:
                emma_probability[first + second] += 1

    gunnar_total = 0
    emma_total = 0

    for p in gunnar_probability:
        gunnar_total += gunnar_probability[p]

    for p in emma_probability:
        emma_total += emma_probability[p]

    expected_gunnar = 0
    expected_emma = 0

    for p in gunnar_probability:
        expected_gunnar += p * (float(gunnar_probability[p]) / gunnar_total)
    for p in emma_probability:
        expected_emma += p * (float(emma_probability[p]) / emma_total)

    if expected_gunnar > expected_emma:
        print("Gunnar")
    elif expected_gunnar < expected_emma:
        print("Emma")
    else:
        print("Tie")


def solution():
    gunnar = float(gunnar_dice[0] + gunnar_dice[1]) / 2 + float(gunnar_dice[2] + gunnar_dice[3]) / 2
    emma = float(emma_dice[0] + emma_dice[1]) / 2 + float(emma_dice[2] + emma_dice[3]) / 2

    if gunnar > emma:
        print("Gunnar")
    elif gunnar < emma:
        print("Emma")
    else:
        print("Tie")


solution()
