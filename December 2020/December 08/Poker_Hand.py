hand = input()
strength = 0
rank = 0

for index in range(0, len(hand), 3):
    rank = hand.count(hand[index])
    if rank > strength:
        strength = rank

print(strength)
