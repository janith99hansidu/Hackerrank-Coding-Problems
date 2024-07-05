def getWays(n, c):
    # Length of the c array
    length_c = len(c)

    # Make a dp table to solve
    dp = [[0] * (n + 1) for _ in range(length_c + 1)]

    # Fill first column
    for i in range(length_c + 1):
        dp[i][0] = 1

    # Fill the dp table
    for j in range(1, length_c + 1):
        for i in range(0, n + 1):
            # If we don't take the current coin
            dp[j][i] = dp[j - 1][i]
            # If we take the current coin (only if i >= c[j-1])
            if i >= c[j - 1]:
                dp[j][i] += dp[j][i - c[j - 1]]

    # The number of ways to make the amount n using all length_c coins
    return dp[length_c][n]

if __name__ == '__main__':
   print(getWays(4, [8, 3, 2, 1]))