def grid_walking(n, m, x):
    """
    :param n: size of the grid
    :param m: number of steps
    :param x: starting position
    :return: number of ways can traverse from given steps
    """

    # Create the dp table
    dp = [[0] * (m + 1) for _ in range(n)]

    # Initialize the starting position
    dp[0][x - 1] = 1

    # Fill the grid
    for steps in range(1, m + 1):
        for cells in range(0, n):
            if cells > 0:
                dp[steps][cells] += dp[steps - 1][cells - 1]
            if cells < n - 1:
                dp[steps][cells] += dp[steps - 1][cells + 1]
        print(dp)
    # return the last
    return sum(dp[m][pos] for pos in range(n))


if __name__ == '__main__':
    n = 4  # size of the grid
    m = 3  # number of steps
    x = 3  # starting position

    print(grid_walking(n, m, x))
