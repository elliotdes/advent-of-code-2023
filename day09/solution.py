import re

from utils import get_input

lines = get_input("day09/input.txt").split("\n")


def find_next_number(numbers: list[int]) -> int:
    diff = [numbers[i] - numbers[i - 1] for i in range(1, len(numbers))]
    if all(diff[0] == i for i in diff):
        return numbers[-1] + diff[0]
    else:
        return numbers[-1] + find_next_number(diff)


def find_first_number(numbers: list[int]) -> int:
    diff = [numbers[i] - numbers[i - 1] for i in range(1, len(numbers))]
    if all(diff[0] == i for i in diff):
        return numbers[0] - diff[0]
    else:
        return numbers[0] - find_first_number(diff)


next_nums = []
first_nums = []
for line in lines:
    numbers = [int(i) for i in re.findall(r"(-?\d+)", line)]
    next_num = find_next_number(numbers)
    first_num = find_first_number(numbers)
    next_nums.append(next_num)
    first_nums.append(first_num)

print(sum(next_nums))
print(sum(first_nums))
