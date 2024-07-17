def longestCommonSubsequence(A, B):
    # get the length of the strings
    m, n = len(A), len(B)

    # initialize the dp table with 0s
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # fill the dp table with dynamic programming
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            if A[j - 1] == B[i - 1]:
                dp[j][i] = dp[j - 1][i] + 1
            else:
                dp[j][i] = max(dp[j - 1][i], dp[j][i - 1])

    return dp[m][n]


if __name__ == '__main__':
    A = "AGGTAB"
    B = "GXTXAYB"
    print(longestCommonSubsequence(A, B))
