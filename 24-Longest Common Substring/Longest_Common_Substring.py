def longestCommonSubstring(A, B):
    n, m = len(A), len(B)
    max_substring = 0
    # initialize the dp table with zeros
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # fill the dp table
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[j][i] = dp[j - 1][i - 1] + 1
                max_substring = max(max_substring, dp[j][i])
            else:
                dp[j][i] = 0

    return max_substring


if __name__ == '__main__':
    A = "ABCDGH"
    B = "ACDGHR"
    print(longestCommonSubstring(A, B))
