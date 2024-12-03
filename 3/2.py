import re

lines = open("aoc24/3/input.txt").read()
result = 0
shouldContinue = True

lineCommands = []

for match in re.finditer(r"mul\((-?\d+),(-?\d+)\)", lines):
    lineCommands.append(('mul', match.start(), match.groups()))

for match in re.finditer(r'do\(\)', lines):
    lineCommands.append(('do', match.start(), None))

for match in re.finditer(r'don\'t\(\)', lines):
    lineCommands.append(('dont', match.start(), None))

lineCommands.sort(key = lambda x: x[1])

for command, _, groups in lineCommands:
    if (command == 'do'):
        shouldContinue = True
    elif (command == 'dont'):
        shouldContinue = False
    elif ((command == 'mul') and (shouldContinue)):
        num1, num2 = map(int, groups)

        result += num1 * num2

print(result)

# Itt valami bentől néztem le a patterneket es a go logikajat. :d