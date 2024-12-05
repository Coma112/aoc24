def count_word_occurrences(lines, word):
    rows = len(lines)
    cols = len(lines[0]) if rows > 0 else 0
    word_length = len(word)
    count = 0

    directions = [
        (0, 1), 
        (1, 0), 
        (1, 1),
        (1, -1), 
        (0, -1),
        (-1, 0), 
        (-1, -1), 
        (-1, 1)
    ]

    for r in range(rows):
        for c in range(cols):
            if lines[r][c] == 'X':
                for dr, dc in directions:
                    if all(0 <= r + dr * i < rows and 0 <= c + dc * i < cols and lines[r + dr * i][c + dc * i] == word[i] for i in range(word_length)):
                        count += 1

    return count

if __name__ == "__main__":
    with open("c:/Users/kulas/Desktop/Projektek/Suli/Python/aoc2024/4/input.txt") as file:
        lines = [line.strip() for line in file.readlines()]

    word = "XMAS"
    occurrences = count_word_occurrences(lines, word)
    print(occurrences)