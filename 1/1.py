with open('1/input.txt') as f:
    lines = f.readlines()

leftList = []
rightList = []

for line in lines:
    left, right = map(int, line.split())
    
    leftList.append(left)
    rightList.append(right)

leftList.sort()
rightList.sort()

print(sum(abs(l - r) for l, r in zip(leftList, rightList)))