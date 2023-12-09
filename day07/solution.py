import re
from collections import Counter

from utils import get_input

lines = get_input("day07/input.txt").split("\n")


def determine_hand_type(cards: Counter) -> int:
    if len(cards) == 1:
        return 7
    elif len(cards) == 2:
        if 4 in cards.values():
            return 6
        elif 3 in cards.values():
            return 5
    elif len(cards) == 3:
        if 3 in cards.values():
            return 4
        if 2 in cards.values():
            return 3
    elif len(cards) == 4:
        return 2
    elif len(cards) == 5:
        return 1
    raise ValueError("Unknown hand!")


# part 1
converter = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
hands = []
for line in lines:
    cards, bid = re.findall(r"(\w+) (\d+)", line)[0]
    cards = re.findall(r"(\w)", cards)
    cards = [int(c) if c not in converter else converter[c] for c in cards]
    counter = Counter(cards)
    hand_type = determine_hand_type(counter)
    hands.append((hand_type, cards, int(bid)))

sorted_hands = sorted(hands, key=lambda x: (x[0], x[1]))

total_winnings = 0
for rank, hand in enumerate(sorted_hands):
    bid = hand[2]
    total_winnings += (rank + 1) * bid
print(total_winnings)

# part 2
converter = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}
hands = []
for line in lines:
    cards, bid = re.findall(r"(\w+) (\d+)", line)[0]
    cards = re.findall(r"(\w)", cards)
    cards = [int(c) if c not in converter else converter[c] for c in cards]
    counter = Counter(cards)
    # Special case for all Jokers
    if cards != [1, 1, 1, 1, 1]:
        most_common_card = next(c[0] for c in counter.most_common(5) if c[0] != 1)
        counter[most_common_card] += counter[1]
        counter.pop(1, None)
    hand_type = determine_hand_type(counter)
    hands.append((hand_type, cards, int(bid)))

sorted_hands = sorted(hands, key=lambda x: (x[0], x[1]))

total_winnings = 0
for rank, hand in enumerate(sorted_hands):
    bid = hand[2]
    total_winnings += (rank + 1) * bid
print(total_winnings)
