import math
import re

from utils import get_input

times, distances = get_input("day06/input.txt").split("\n")

times = [int(i) for i in re.findall(r"(\d+)", times)]
distances = [int(i) for i in re.findall(r"(\d+)", distances)]

# part 1

races = list(zip(times, distances))

counts = 1
for time, distance in races:
    count = 0
    for hold_t in range(1, time):
        velocity = hold_t
        race_t = time - hold_t
        boat_distance = velocity * race_t
        if boat_distance > distance:
            count += 1
    counts *= count

print(counts)

# part 2
time = int("".join(map(str, times)))
distance = int("".join(map(str, distances)))
min_x = (time - math.sqrt(time**2 - 4 * 1 * distance)) / (2 * 1)
max_x = (time + math.sqrt(time**2 - 4 * 1 * distance)) / (2 * 1)
print(math.floor(max_x) - math.ceil(min_x) + 1)
