def commonChild(s1, s2):
    # Write your code here
    len_st = len(s1)
    # get the longest common substring
    dp = [[0] * (len_st + 1) for _ in range(len_st + 1)]

    # fill the dp table
    for j in range(1, len_st + 1):
        for i in range(1, len_st + 1):

            if s1[j - 1] == s2[i - 1]:
                dp[j][i] = dp[j - 1][i - 1] + 1
            else:
                dp[j][i] = max(dp[j - 1][i], dp[j][i - 1])

    return dp[len_st][len_st]


if __name__ == '__main__':
    print(commonChild("SHINCHAN", "NOHARAAA"))
