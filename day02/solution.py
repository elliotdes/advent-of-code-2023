import re

from utils import get_input

lines = get_input("day02/input.txt").split("\n")

bc_limit = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

possible_ids = []
game_power = []
for line in lines:
    all_cubes: dict[str, list[int]] = {"red": [], "green": [], "blue": []}
    possible = True
    game_id = int(re.findall("Game (\d+)", line)[0])
    sets = line.split(";")
    for s in sets:
        balls = re.findall("(\d+) (\w+)", line)
        for cnt, colour in balls:
            if int(cnt) > bc_limit[colour]:
                possible = False
            all_cubes[colour].append(int(cnt))

    if possible:
        possible_ids.append(game_id)
    game_power.append(
        max(all_cubes["red"]) * max(all_cubes["green"]) * max(all_cubes["blue"])
    )

# part 1
print(sum(possible_ids))
# part 2
print(sum(game_power))
