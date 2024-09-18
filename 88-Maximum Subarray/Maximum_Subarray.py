def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    total_max = nums[0]
    len_num = len(nums)

    # make dp array to store current maximum
    dp = [0] * len_num

    # initialize the dp
    dp[0] = nums[0]

    # traverse from the beginning and populate the dp array
    for i in range(1,len_num):
        dp[i] = max(dp[i-1]+nums[i], nums[i])

        if dp[i] > total_max:
            total_max = dp[i]

    return total_max


if __name__ == '__main__':
    maxSubArray([-2,1,-3,4,-1,2,1,-5,4])