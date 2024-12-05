def find_xmas(grid):
    x_dirs = [(0, 0), (1, 1), (2, 2), (0, 2), (2, 0)]
    patterns = [
        "MASSM",
        "MASMS",
        "SAMSM",
        "SAMMS"
    ]

    def check_patterns(r, c):
        if not (0 <= r + 2 < len(grid) and 0 <= c + 2 < len(grid[0])):
            return False
        
        return any(
            all(
                grid[r + x_dirs[i][0]][c + x_dirs[i][1]] == p[i]
                for i in range(5)
            )
            for p in patterns
        )

    count = sum(
        check_patterns(r, c)
        for r in range(len(grid))
        for c in range(len(grid[0]))
    )

    return count

if __name__ == "__main__":
    with open("c:/Users/kulas/Desktop/Projektek/Suli/Python/aoc2024/4/input.txt") as file:
        lines = [line.strip() for line in file.readlines()]
    print(find_xmas(lines))