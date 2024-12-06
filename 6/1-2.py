from dataclasses import dataclass

@dataclass(frozen=True)
class Position:
    i: int
    j: int

    def __add__(self, other):
        return Position(self.i + other.i, self.j + other.j)

    def __eq__(self, other):
        return isinstance(other, Position) and (self.i, self.j) == (other.i, other.j)

    def __hash__(self):
        return hash((self.i, self.j))

    def rotate_right(self):
        return Position(self.j, -self.i)

def is_within_bounds(position, n, m):
    return 0 <= position.i < n and 0 <= position.j < m

def get_guard_span(grid, start, new_obstacle=None):
    position = Position(*start)
    direction = Position(-1, 0)
    visited = set()
    states = {(position, direction)}

    while is_within_bounds(position, len(grid), len(grid[0])):
        visited.add(position)
        next_position = position + direction
        
        if is_within_bounds(next_position, len(grid), len(grid[0])) and (grid[next_position.i][next_position.j] == '#' or next_position == new_obstacle):
            direction = direction.rotate_right()
        else:
            position = next_position
        
        new_state = (position, direction)
        if new_state in states:
            return True, visited
        states.add(new_state)
    
    return False, visited

def main():
    grid = []
    with open('aoc2024/6/input.txt', 'r') as f:
        for i, line in enumerate(f):
            row = line.strip()
            if '^' in row:
                start = (i, row.find('^'))
                row = row.replace('^', '.')
            grid.append(row)
    
    visited_positions = get_guard_span(grid, start)[1]
    print(f"1: {len(visited_positions)}")

    obstacle_candidates = visited_positions - {Position(*start)}
    result = sum(1 for obstacle in obstacle_candidates if get_guard_span(grid, start, obstacle)[0])
    
    print(f"2: {result}")

if __name__ == "__main__":
    main()

# Nagyon lassú a második rész. Annyira nem látom még át a python-t mint amennyire kéne a feladathoz de. Megvan és én találtam ki a megoldását :)