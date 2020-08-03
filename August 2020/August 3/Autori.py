name = input()

autori = ""

for letter in name:
    if letter.isupper():
        autori += letter

print(autori)
