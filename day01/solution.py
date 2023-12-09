import re

from utils import get_input

lines = get_input("day01/input.txt").split("\n")

# part 1

# digits = [re.findall("\d", line) for line in lines]
# numbers = [int(f"{d[0]}{d[-1]}") for d in digits]

# print(sum(numbers))

# part 2

word_to_number = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

# overlapping regex - lookahead assertion
pattern = "(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
digits = [re.findall(pattern, line) for line in lines]

summed = 0
for d in digits:
    number = ""
    for idx in [0, -1]:
        i = d[idx]
        if i in word_to_number:
            number += str(word_to_number[i])
        else:
            number += i
    summed += int(number)


print(summed)
