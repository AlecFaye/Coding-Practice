import copy


def my_solution():
    list_length = int(input())

    while list_length != 0:
        first_list = []
        second_list = []

        for count in range(list_length):
            first_list.append(int(input()))

        for count in range(list_length):
            second_list.append(int(input()))

        first_copy = copy.deepcopy(first_list)
        first_copy.sort()
        second_list.sort()

        for count in range(list_length):
            number = first_list[count]
            index = first_copy.index(number)
            print(second_list[index])
        print()

        list_length = int(input())


my_solution()
