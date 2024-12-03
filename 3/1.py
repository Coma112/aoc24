import re

with open('aoc24/3/input.txt') as f:
    lines = f.readlines()

result = 0

for line in lines:
    for i in re.findall(r"mul\((-?\d+),(-?\d+)\)", line):
        num1, num2 = map(int, i)
        result += num1 * num2

print(result)