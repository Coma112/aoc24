with open('aoc24/2/input.txt') as f:
    lines = f.readlines()

safeCount = 0

def isSafe(numberRange: str):
    numberList = list(map(int, numberRange.split(" ")))
    
    isIncreasing = True
    isDecreasing = True
    
    for i in range(len(numberList) - 1):
        difference = abs(numberList[i] - numberList[i + 1])
        
        if difference < 1 or difference > 3:
            return False
        
        if numberList[i] < numberList[i + 1]:
            isDecreasing = False
        elif numberList[i] > numberList[i + 1]:
            isIncreasing = False
    
    return isIncreasing or isDecreasing

for line in lines:
    if isSafe(line):
        safeCount += 1

print(safeCount)