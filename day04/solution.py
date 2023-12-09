import re
from collections import defaultdict

from utils import get_input

lines = get_input("day04/input.txt").split("\n")


def num_worth(num: int) -> int:
    if num == 0:
        return 0
    return 2 ** (num - 1)


worths = []
cards: dict[int, int] = defaultdict(int)
card_winnings: dict[int, int]
for line in lines:
    card_no = int(re.findall(r"Card\s+(\d+)", line)[0])
    # always get original instance of card
    cards[card_no] += 1
    numbers, winning = line.split("|")
    numbers = set(re.findall(r"(\d+) ", numbers))
    winning = re.findall(r" (\d+)", winning)
    worth_cnt = 0
    for c in winning:
        if c in numbers:
            worth_cnt += 1
            cards[card_no + worth_cnt] += 1 * (cards[card_no])
    worths.append(num_worth(worth_cnt))

# part 1
print(sum(worths))
# part 2
print(sum(cards.values()))
