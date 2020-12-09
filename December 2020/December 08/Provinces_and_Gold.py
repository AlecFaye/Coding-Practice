gold, silver, copper = list(map(int, input().split()))
buying_power = gold * 3 + silver * 2 + copper * 1

if buying_power >= 8:
    print("Province or Gold")
elif buying_power >= 6:
    print("Duchy or Gold")
elif buying_power >= 5:
    print("Duchy or Silver")
elif buying_power >= 3:
    print("Estate or Silver")
elif buying_power >= 2:
    print("Estate or Copper")
else:
    print("Copper")
