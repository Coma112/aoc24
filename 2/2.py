lines = open("aoc24/2/input.txt").read().splitlines()
safeCount = 0

def isSafe(levels):
    numberList = list(map(int, levels.split(" ")))
    
    for i in range(len(numberList) - 1):
        difference = abs(numberList[i] - numberList[i + 1])
        
        if ((difference < 1) or (difference > 3)):
            return False
    
    return all(earlier < later for earlier, later in zip(numberList, numberList[1:])) or all(earlier >= later for earlier, later in zip(numberList, numberList[1:]))

def canBeMadeSafe(levels):
    levelList = list(map(int, levels.split(" ")))
    
    for i in range(len(levelList)):
        newLevels = levelList[:i] + levelList[i + 1:]

        if (isSafe(" ".join(map(str, newLevels)))):
            return True
    return False

for line in lines:
    line = line.strip()

    if (isSafe(line)):
        safeCount += 1
    elif (canBeMadeSafe(line)):
        safeCount += 1

print(safeCount)