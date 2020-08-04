phrase = input().split()

words = []
repeat = False

for word in phrase:
    if word not in words:
        words.append(word)
    else:
        repeat = True

if repeat:
    print("no")
else:
    print("yes")
