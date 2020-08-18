import math

cases = int(input())

for test in range(cases):
    encoded_message = input()
    side_length = int(math.sqrt(len(encoded_message)))

    message_array = []

    for i in range(0, len(encoded_message), side_length):
        line = []
        for j in range(side_length):
            line.append(encoded_message[i + j])
        message_array.append(line)

    decoded_message = ""

    for col in range(side_length - 1, -1, -1):
        for row in range(side_length):
            decoded_message += message_array[row][col]

    print(decoded_message)
