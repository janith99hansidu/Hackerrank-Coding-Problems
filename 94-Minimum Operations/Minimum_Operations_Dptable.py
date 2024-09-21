def minOperation(k):
    # make array of
    dp = [float('inf')] * (k+1)
    dp[1] = 1

    # traverse from 1 to the k-1 position to update the values iteratively
    for i in range(1, k):

        # add one to the dp[i] to step one
        jump_pos_add_one = i + 1
        jump_pos_mul_one = i*2

        # check the value is smaller than value at the position
        if dp[i]+1 < dp[jump_pos_add_one]:
            # add previous value + 1 to the current
            dp[jump_pos_add_one] = dp[i]+1

        if jump_pos_mul_one <= k:
            # add the previous value + 1 if the position is value is greater than current value
            if dp[i] + 1 < dp[jump_pos_mul_one]:
                dp[jump_pos_mul_one] = dp[i] + 1

    return dp[k]


if __name__ == '__main__':
    print(minOperation(4))
