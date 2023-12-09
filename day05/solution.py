import re

from utils import get_input

maps = get_input("day05/input.txt").split("\n\n")

# part 1
seeds = [int(i) for i in re.findall(r"(\d+)", maps[0])]

locs = []
for s in seeds:
    for m in maps[1:]:
        m = m.split("\n")
        for r in m[1:]:
            d_start, s_start, r_len = [int(i) for i in re.findall(r"(\d+)", r)]
            s_end = s_start + r_len
            if s_start <= s < s_end:
                s = d_start + (s - s_start)
                break
    locs.append(s)
print(min(locs))


def process_range(sr: tuple[int, int], r: tuple[int, int], t: int) -> bool:
    if sr[0] >= r[0] and sr[1] <= r[1]:
        # sr is completely within r
        processed.append((sr[0] + t, sr[1] + t))
        return True
    elif sr[0] > r[0] and r[1] > sr[0]:
        # right side of sr is not processed
        processed.append((sr[0] + t, r[1] + t))
        to_process.append((r[1], sr[1]))
        return True
    elif sr[0] >= r[0] and sr[1] < r[1]:
        # left side of sr is not processed
        processed.append((r[0] + t, sr[1] + t))
        to_process.append((sr[1], r[1]))
        return True
    elif sr[0] < r[0] and sr[1] > r[1]:
        # right and left side of sr are not processed
        processed.append((r[0] + t, r[1] + t))
        to_process.append((sr[0], r[0]))
        to_process.append((r[1], sr[1]))
        return True
    return False


to_process = list(zip(seeds[0::2], seeds[1::2]))
to_process = [(i[0], i[0] + i[1]) for i in to_process]

for m in maps[1:]:
    processed: list[tuple[int, int]] = []
    m = m.split("\n")
    while to_process:
        handled = False
        sr = to_process.pop()
        for r in m[1:]:
            d_start, s_start, r_len = [int(i) for i in re.findall(r"(\d+)", r)]
            rng = (s_start, s_start + r_len)
            transform = d_start - s_start
            if process_range(sr, rng, transform):
                handled = True
        if not handled:
            processed.append(sr)

    to_process = processed.copy()

print(min(i[0] for i in processed))
