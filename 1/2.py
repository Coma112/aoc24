from collections import Counter

with open('1/input.txt') as f:
    lines = f.readlines()

leftList = []
rightList = []

for line in lines:
    left, right = map(int, line.split())
    
    leftList.append(left)
    rightList.append(right)

print(sum(num * Counter(rightList)[num] for num in leftList))