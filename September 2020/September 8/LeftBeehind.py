sweet, sour = map(int, input().split())

while sweet != 0 or sour != 0:
    if sweet + sour == 13:
        print("Never speak again.")
    elif sweet < sour:
        print("Left beehind.")
    elif sweet > sour:
        print("To the convention.")
    else:
        print("Undecided.")

    sweet, sour = map(int, input().split())
