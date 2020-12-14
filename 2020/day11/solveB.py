import sys
from itertools import product

def parse_input(lines):
    grid = [[char for char in line.strip()] for line in lines]
    return grid

def pair_plus(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])

def count_neighbors(grid, i, j):
    assert grid[i][j] != '.'
    if not grid:
        return 0
    neighbors = 0
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if (x, y) == (0, 0):
                continue
            r, c = i, j
            while True:
                r, c = pair_plus((r,c), (x,y))
                if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                    break
                if grid[r][c] != '.':
                    neighbors += 1 if grid[r][c] == '#' else 0
                    break
    return neighbors

def update_grid(grid):
    new_grid = [[cell for cell in row] for row in grid]
    neighbor_grid = [[cell for cell in row] for row in grid]
    changed = False
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell != '.':
                neighbors = count_neighbors(grid, i, j)
                neighbor_grid[i][j] = str(neighbors)
                if neighbors == 0:
                    new_grid[i][j] = '#'
                elif neighbors >= 5:
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
        changed, grid = update_grid(grid)
        if not changed:
            break

    print(count_occupied(grid))

if __name__ == '__main__':
    main()


