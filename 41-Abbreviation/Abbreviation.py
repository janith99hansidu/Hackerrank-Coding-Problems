def abbreviation(a, b):
    # make the dp table
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    # initialize the first cell with 1 (empty string case)
    dp[0][0] = 1

    # initialize the first column
    for i in range(1, len(a) + 1):
        if a[i - 1].islower():
            dp[i][0] = dp[i - 1][0]
        else:
            dp[i][0] = 0

    # fill the dp table
    for j in range(1, len(a) + 1):
        for i in range(1, len(b) + 1):
            # if the letters are same and previously match without that element
            if a[j - 1].upper() == b[i - 1]:
                dp[j][i] = dp[j - 1][i - 1] or (dp[j - 1][i] if a[j - 1].islower() else 0)
            else:
                if a[j - 1].islower():
                    dp[j][i] = dp[j - 1][i]

    # check the last element is true otherwise it is false
    if dp[len(a)][len(b)] == 1:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    print(abbreviation("MXCXHIBQFIXTJMHURXCHHKVHUtfydvznieoivbuflfvsyfizoffajspejbagwxsmaxkp", "MXCXHIBQFIXTJMHURXCHHKVHU"))
