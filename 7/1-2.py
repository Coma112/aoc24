from functools import lru_cache

with open('aoc2024/7/input.txt') as f:
    lines = [x.strip().split(':') for x in f]

testVals = [int(line[0]) for line in lines]
equations = [list(map(int, line[1].split())) for line in lines]

calc = lambda eqs, ops: eval(
    "".join(
        str(eqs[0]) + "".join(op + str(eq) for op, eq in zip(ops, eqs[1:]))
    ).replace('|', ''))

def solve(eqs, target, operators):
    @lru_cache(None)
    def explore(index, current):
        if index == len(eqs):
            return current == target
        for op in operators:
            nextValue = (
                current + eqs[index] if op == '+' else
                current * eqs[index] if op == '*' else
                int(str(current) + str(eqs[index]))
            )
            if op == '|' and nextValue > target:
                continue
            if explore(index + 1, nextValue):
                return True
        return False
    return explore(1, eqs[0])

result1 = lambda: (
    sum(val for val, eq in zip(testVals, equations) if solve(eq, val, ('+', '*'))),
    sum(1 for val, eq in zip(testVals, equations) if solve(eq, val, ('+', '*')))
)

result2 = lambda: (
    sum(val for val, eq in zip(testVals, equations) if solve(eq, val, ('+', '*', '|'))),
    sum(1 for val, eq in zip(testVals, equations) if solve(eq, val, ('+', '*', '|')))
)

print(result1())
print(result2())