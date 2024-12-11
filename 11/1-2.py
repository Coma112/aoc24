from functools import cache

def parse(data):
    return [int(d) for d in data.split()]


@cache
def count(stone, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return count(1, steps - 1)
    str_stone = str(stone)
    if len(str_stone) % 2 == 0:
        half = len(str_stone) // 2
        return count(int(str_stone[:half]), steps - 1) + count(int(str_stone[half:]), steps - 1)
    return count(stone * 2024, steps - 1)


def part1(data):
    return sum(count(stone, 25) for stone in data)


def part2(data):
    return sum(count(stone, 75) for stone in data)


data = open('aoc24/11/input.txt').read().strip()
print(part1(parse(data)))
print(part2(parse(data)))