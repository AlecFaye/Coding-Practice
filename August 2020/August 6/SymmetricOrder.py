set_count = int(input())
current_set = 1

while set_count != 0:
    name_array = []

    for count in range(set_count):
        name_array.append("Default")

    increment = 0

    for count in range(set_count):
        if count % 2 == 0:
            name_array[count - increment] = input()
        else:
            name_array[set_count - count + increment] = input()
            increment += 1

    print("SET " + str(current_set))
    for name in name_array:
        print(name)

    current_set += 1
    set_count = int(input())
