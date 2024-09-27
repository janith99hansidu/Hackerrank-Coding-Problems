# not efficient for CS academy
def lcs(s1, s2):
    # make the relevant variables
    s1_len = len(s1)
    s2_len = len(s2)

    # make the dp array
    dp = [[0] * (s1_len + 1) for _ in range(s2_len + 1)]

    # fill the dp table with the given conditions
    for row in range(1, s2_len + 1):
        for column in range(1, s1_len + 1):

            # if the current s1 and s2 are same element copy from diagonal
            if s1[column - 1] == s2[row - 1]:
                dp[row][column] = dp[row - 1][column - 1] + 1
            else:
                dp[row][column] = max(dp[row - 1][column], dp[row][column - 1])

    return dp[s2_len][s1_len]


if __name__ == '__main__':
    # Read the input
    s = input().strip()
    q = int(input().strip())

    # Process each query
    for _ in range(q):
        p = input().strip()
        # Find the longest suffix of p that is a subsequence of s
        result = lcs(s, p)
        print(result)
