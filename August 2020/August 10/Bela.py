hand_dominate = input().split()

hand_count = int(hand_dominate[0])
dominant_suit = hand_dominate[1]

dominant_card_values = {
    "A": 11,
    "K": 4,
    "Q": 3,
    "J": 20,
    "T": 10,
    "9": 14,
    "8": 0,
    "7": 0
}

non_dominant_card_values = {
    "A": 11,
    "K": 4,
    "Q": 3,
    "J": 2,
    "T": 10,
    "9": 0,
    "8": 0,
    "7": 0
}

total_points = 0

for count in range(hand_count * 4):
    hand = input()
    card = hand[0]
    suit = hand[1]

    if suit == dominant_suit:
        total_points += dominant_card_values[card]
    else:
        total_points += non_dominant_card_values[card]

print(total_points)
