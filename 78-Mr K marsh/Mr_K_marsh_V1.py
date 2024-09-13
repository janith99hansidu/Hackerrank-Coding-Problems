def kMarsh(grid):
    # Write your code here
    rows = len(grid)
    cols = len(grid[0])

    # largest perimeter variable
    largest_perimeter = -1

    # traverse all possible combinations of rows
    for r1 in range(rows):
        for r2 in range(r1 + 1, rows):

            valid_col = []
            # find the valid columns both have '.' find edge position up_left and up_right
            for c in range(cols):
                if grid[r1][c] == '.' and grid[r2][c] == '.':
                    valid_col.append(c)

            # check every pair form a valid rectangular
            for i in range(len(valid_col)):
                for j in range(i + 1, len(valid_col)):
                    c1, c2 = valid_col[i], valid_col[j]

                    is_valid = True
                    for k in range(c1 + 1, c2):
                        if grid[r1][k] == 'x' or grid[r2][k] == 'x':
                            is_valid = False
                            break

                    if is_valid:
                        width = c2 - c1
                        height = r2 - r1
                        perimeter = 2 * (width + height)
                        largest_perimeter = max(largest_perimeter, perimeter)

    if largest_perimeter == -1:
        print("impossible")
    else:
        print(largest_perimeter)


if __name__ == '__main__':
    grid = [[".", ".", ".", ".", "."],
            [".", "x", ".", "x", "."],
            [".", ".", ".", ".", "."],
            [".", ".", ".", ".", "."]]
    kMarsh(grid)
