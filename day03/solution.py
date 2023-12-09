import re
from collections import defaultdict

from utils import get_input

lines = get_input("day03/example.txt").split("\n")


def get_adjacent(y: int, x_start: int, x_end: int) -> tuple[str, set[tuple[int, int]]]:
    adjacent = ""
    gears: set[tuple[int, int]] = set()
    for x in range(x_start, x_end):
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                new_x = x + dx
                new_y = y + dy
                if new_x >= 0 and new_y >= 0 and (new_x, new_y) != (x, y):
                    try:
                        character = lines[new_y][new_x]
                        adjacent += character
                        if character == "*":
                            gears.add((new_x, new_y))
                    except IndexError:
                        pass

    return adjacent, gears


part_numbers = []
all_gears: dict[tuple[int, int], list[int]] = defaultdict(list)

for y, line in enumerate(lines):
    matches = re.finditer(r"\d+", line)
    for match in matches:
        number = match.group()
        index = match.start()
        adjacent, gears = get_adjacent(y, index, index + len(number))
        if bool(re.search(r"[^\d\.]", adjacent)):
            part_numbers.append(int(number))
            for gear in gears:
                all_gears[gear].append(int(number))

# part 1
print(sum(part_numbers))

# part 2
gear_sum = 0
for gear_numbers in all_gears.values():
    if len(gear_numbers) == 2:
        gear_ratio = gear_numbers[0] * gear_numbers[1]
        gear_sum += gear_ratio
print(gear_sum)
