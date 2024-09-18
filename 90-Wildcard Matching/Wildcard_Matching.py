def isMatch(s, p):
    len_s = len(s)
    len_p = len(p)

    # make a dp table to find all possible cases
    dp = [[False]*(len_s+1) for _ in range(len_p+1)]

    # make first cell true
    dp[0][0] = True
    # handle * at the beginning
    for row in range(1, len_p + 1):
        if p[row - 1] == '*':
            dp[row][0] = dp[row - 1][0]

    # iterate each cell and fill up the dp table
    # rows are pattern
    # columns are
    for row in range(1, len_p+1):
        for column in range(1, len_s+1):

            # if it is a letter check for the previous is true
            if p[row-1].islower() and p[row-1] == s[column-1] and dp[row-1][column-1]:
                dp[row][column] = True

            # if the pattern is ? then check the previous state is true or false
            if p[row-1] == '?' and dp[row-1][column-1]:
                dp[row][column] = True

            # check for the *
            if p[row-1] == '*' and (dp[row-1][column] or dp[row][column-1]) :
                dp[row][column] = True

    return 'true' if dp[len_p][len_s] else 'false'


if __name__ == '__main__':
    print(isMatch("acdcb","a*c?b"))
    print(isMatch("cb", "?a"))
    print(isMatch("aa", "?a"))
    print(isMatch("aa", "*"))