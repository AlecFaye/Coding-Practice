while True:
    try:
        integers = input().split()

        total_sum = 0
        answer_index = -1

        while total_sum != int(integers[answer_index]):
            total_sum = 0
            answer_index += 1

            for index in range(len(integers)):
                if index != answer_index:
                    total_sum += int(integers[index])

        print(integers[answer_index])
    except EOFError:
        break
