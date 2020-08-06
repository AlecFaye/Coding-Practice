cases = int(input())

encounter = {
    "b": "$",
    "j": "*",
    "t": "|"
}

objects = ["$", "*", "|"]

for test in range(cases):
    backpack = []
    complete_adventure = True

    adventure = input()

    for event in adventure:
        if event in objects:
            backpack.append(event)
        elif event in encounter:
            if len(backpack) > 0:
                index = len(backpack) - 1
                if backpack[index] == encounter[event]:
                    backpack.pop(index)
                else:
                    complete_adventure = False
            else:
                complete_adventure = False

    if len(backpack) > 0:
        complete_adventure = False

    if complete_adventure:
        print("YES")
    else:
        print("NO")
