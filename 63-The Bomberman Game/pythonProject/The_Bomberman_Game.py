def bomberMan(n, grid):
    # Write your code here
    # covert string to 2d list for easy manipulation
    current_grid_2d_array = [list(row) for row in grid]
    rows = len(current_grid_2d_array)
    columns = len(current_grid_2d_array[0])

    # n-2 state array of the 2d array
    n_two_state_2d_array = [['.'] * columns for _ in range(rows)]

    for steps in range(1, n+1):
        if n % 2 == 0:
            for i in 



# if current_grid_2d_array[i][j] == sample_2d_array[i][j]:
#     n_two_state_2d_array[i][j] = '.'
#     if i - 1 >= 0:
#         n_two_state_2d_array[i - 1][j] = '.'
#     if i + 1 < rows:
#         n_two_state_2d_array[i + 1][j] = '.'
#     if j - 1 >= 0:
#         n_two_state_2d_array[i][j - 1] = '.'
#     if j + 1 < columns:
#         n_two_state_2d_array[i][j + 1] = '.'

if __name__ == '__main__':
    r = 6
    c = 7
    n = 3
    grid = [
        ".......",
        "...O...",
        "....O..",
        ".......",
        "OO.....",
        "OO....."
    ]
    bomberMan(n, grid)
