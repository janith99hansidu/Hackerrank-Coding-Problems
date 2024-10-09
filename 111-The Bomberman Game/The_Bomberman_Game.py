import os

def bomberMan(n, grid):
    def explode(current_grid):
        # create a new grid initialized with all bombs
        row, col = len(current_grid), len(current_grid[0])
        next_grid = [['O'] * col for _ in range(row)]

        # traverse the current grid to apply bomb explosions
        for r in range(row):
            for c in range(col):
                if current_grid[r][c] == 'O':
                    next_grid[r][c] = '.'
                    if r - 1 >= 0:
                        next_grid[r-1][c] = '.'
                    if r + 1 < row:
                        next_grid[r+1][c] = '.'
                    if c - 1 >= 0:
                        next_grid[r][c-1] = '.'
                    if c + 1 < col:
                        next_grid[r][c+1] = '.'
        return next_grid

    if n == 1:
        return grid
    elif n % 2 == 0:
        # all bombs are planted
        return ['O' * len(grid[0]) for _ in range(len(grid))]
    else:
        # simulate explosions
        grid_after_first_explosion = explode(grid)
        grid_after_second_explosion = explode(grid_after_first_explosion)
        
        # n % 4 = 3 means return first explosion, otherwise second explosion
        if n % 4 == 3:
            return [''.join(row) for row in grid_after_first_explosion]
        else:
            return [''.join(row) for row in grid_after_second_explosion]

if __name__ == '__main__':
    # Convert input to integers using map
    r, c, n = map(int, input().split())
    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    print(bomberMan(n, grid))
