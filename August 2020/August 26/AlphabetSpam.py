phrase = input()
phrase = [char for char in phrase]

whitespace = 0
lowercase = 0
uppercase = 0
symbols = 0

for letter in phrase:
    if 65 <= ord(letter) <= 90:
        uppercase += 1
    elif 97 <= ord(letter) <= 122:
        lowercase += 1
    elif letter == "_":
        whitespace += 1
    else:
        symbols += 1

print(float(whitespace) / len(phrase))
print(float(lowercase) / len(phrase))
print(float(uppercase) / len(phrase))
print(float(symbols) / len(phrase))
