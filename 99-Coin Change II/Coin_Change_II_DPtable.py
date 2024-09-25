def change(amount, coins):
    n_col = amount + 1
    n_row = len(coins) + 1
    # make dp table to populate bottom up approach
    dp = [[0] * n_col for _ in range(n_row)]

    # initialize the first row as 1
    for row in range(n_row):
        dp[row][0] = 1

    # populate the dp table
    for r in range(1, n_row):
        for c in range(1, n_col):

            if coins[r - 1] <= c:
                # sum the ways by including the coin and excluding the coin
                dp[r][c] = dp[r][c - coins[r - 1]] + dp[r - 1][c]
            else:
                # copy the value from the row above (exclude the coin)
                dp[r][c] = dp[r - 1][c]

    return dp[n_row-1][n_col-1]


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 5

    print(change(amount, coins))
