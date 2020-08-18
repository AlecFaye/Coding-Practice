sentence = input()

vowels = ["a", "e", "i", "o", "u"]

decoded_message = ""
skip_index = 0

for index in range(len(sentence)):
    if index + skip_index < len(sentence):

        letter = sentence[index + skip_index]

        if letter in vowels:
            skip_index += 2

        decoded_message += letter

print(decoded_message)
