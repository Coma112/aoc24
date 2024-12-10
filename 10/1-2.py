grid = []
with open('aoc24/10/input.txt', 'r') as file:
    for line in file:
        grid.append(list(line.strip()))

rows = len(grid)
cols = len(grid[0])

start_points = [(i, j) for i in range(rows) for j in range(cols) if grid[i][j] == '0']

def get_neighbors(coord):
    i, j = coord
    potential_neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    return [(x, y) for (x, y) in potential_neighbors if 0 <= x < rows and 0 <= y < cols and int(grid[x][y]) == int(grid[i][j]) + 1]

def bfs_distance(start):
    visited = {start}
    distances = {}
    queue = [start]
    distances[start] = 0

    while queue:
        current = queue.pop(0) 
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                distances[neighbor] = distances[current] + 1

    return distances

part1_count = 0
for start in start_points:
    distances = bfs_distance(start)
    part1_count += sum(1 for distance in distances.values() if distance == 9)

print('Part 1:', part1_count)

def dfs_paths(current, goal, visited, path):
    if current == goal:
        yield path

    for neighbor in get_neighbors(current):
        if neighbor not in visited:
            new_visited = visited.copy()
            new_visited.add(neighbor)
            yield from dfs_paths(neighbor, goal, new_visited, path + [neighbor])

part2_count = 0
for start in start_points:
    distances = bfs_distance(start)
    for target, distance in distances.items():
        if distance == 9:
            part2_count += len(list(dfs_paths(start, target, {start}, [start])))

print('Part 2:', part2_count)