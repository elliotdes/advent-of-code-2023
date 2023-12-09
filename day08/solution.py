import math
import re

from utils import get_input

lines = get_input("day08/input.txt").split("\n")

current = "AAA"
destination = "ZZZ"

instructions = re.findall(r"(\w)", lines[0])
instructions = [0 if i == "L" else 1 for i in instructions]

nodes: dict[str, tuple[str, str]] = {}
current_nodes: list[str] = []
for line in lines[2:]:
    node, left, right = re.findall(r"(\w{3})", line)
    nodes[node] = (left, right)
    if node.endswith("A"):
        current_nodes.append(node)

# part 1
steps = 0
while current != destination:
    index = instructions[steps % len(instructions)]
    current = nodes[current][index]
    steps += 1
print(steps)

# part 2
first_seq: list[int] = []
for i, current in enumerate(current_nodes):
    steps = 0
    while not current.endswith("Z"):
        index = instructions[steps % len(instructions)]
        current = nodes[current][index]
        steps += 1
    first_seq.append(steps)

print(math.lcm(*first_seq))
