from collections import defaultdict
from itertools import product

with open('aoc2024/8/input.txt', 'r') as f:
    mat = f.read().splitlines()

rows, cols = len(mat), len(mat[0])
antennas = defaultdict(set)

for x, y in product(range(rows), range(cols)):
    if mat[x][y] != '.':
        antennas[mat[x][y]].add((x, y))

def find_unique_antinode_positions(include_resonance=False):
    def valid(x, y): return 0 <= x < rows and 0 <= y < cols
    antinodes = set()

    for positions in antennas.values():
        for (x1, y1), (x2, y2) in product(positions, repeat=2):
            if (x1, y1) == (x2, y2): 
                continue

            dx, dy = x1 - x2, y1 - y2
            candidates = {(x1 + dx, y1 + dy), (x2 - dx, y2 - dy)}

            if include_resonance:
                while valid(x1 + dx, y1 + dy) or valid(x2 - dx, y2 - dy):
                    x1, y1, x2, y2 = x1 + dx, y1 + dy, x2 - dx, y2 - dy
                    candidates.update({(x1, y1), (x2, y2)})

            antinodes.update((x, y) for x, y in candidates if valid(x, y))

    return len(antinodes)

print(find_unique_antinode_positions())
print(find_unique_antinode_positions(True))
