with open('aoc24/2/input.txt') as f:
    lines = f.readlines()

safeCount = 0

def isSafe(levels):
    numberList = list(map(int, levels.split(" ")))
    
    isIncreasing = True
    isDecreasing = True
    
    for i in range(len(numberList) - 1):
        difference = abs(numberList[i] - numberList[i + 1])
        
        if ((difference < 1) or (difference > 3)):
            return False
        
        if (numberList[i] < numberList[i + 1]):
            isDecreasing = False
        elif (numberList[i] > numberList[i + 1]):
            isIncreasing = False
    
    return isIncreasing or isDecreasing

def canBeMadeSafe(levels):
    levelList = list(map(int, levels.split(" ")))
    n = len(levelList)
    
    for i in range(n):
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