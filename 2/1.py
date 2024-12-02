with open('aoc24/2/input.txt') as f:
    lines = f.readlines()

safeCount = 0

def isSafe(levels):
    numberList = list(map(int, levels.split(" ")))
    
    for i in range(len(numberList) - 1):
        difference = abs(numberList[i] - numberList[i + 1])
        
        if ((difference < 1) or (difference > 3)):
            return False
    
    return all(earlier < later for earlier, later in zip(numberList, numberList[1:])) or all(earlier >= later for earlier, later in zip(numberList, numberList[1:]))

for line in lines:
    if isSafe(line):
        safeCount += 1

print(safeCount)