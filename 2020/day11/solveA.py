import sys
from itertools import product

def parse_input(lines):
    grid = [[char for char in line.strip()] for line in lines]
    return grid

def count_neighbors(grid, i, j):
    assert grid[i][j] != '.'
    if not grid:
        return 0
    neighbors = 0
    for x in (i-1, i, i+1):
        if x < 0 or x >= len(grid):
            continue
        for y in (j-1, j, j+1):
            if y < 0 or y >= len(grid[0]):
                continue
            if x == i and y == j:
                continue
            neighbors += 1 if grid[x][y] == '#' else 0
    return neighbors

def update_grid(grid):
    new_grid = [[cell for cell in row] for row in grid]
    changed = False
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell != '.':
                neighbors = count_neighbors(grid, i, j)
                if neighbors == 0:
                    new_grid[i][j] = '#'
                elif neighbors >= 4:
                    new_grid[i][j] = 'L'
                changed = True if new_grid[i][j] != grid[i][j] else changed
    return (changed, new_grid)

def count_occupied(grid):
    count = 0
    for row in grid:
        for cell in row:
            if cell == '#':
                count += 1
    return count

def print_grid(grid):
    print("---- GRID -----")
    for row in grid:
        print(' '.join(row))


def main():
    grid = parse_input(sys.stdin)
    while True:
        old_grid = grid
        changed, grid = update_grid(grid)
        if not changed:
            break

    print(count_occupied(grid))

if __name__ == '__main__':
    main()


