import math


def jump(nums):
    len_nums = len(nums)

    # make dp table array
    dp = [float('inf')] * len_nums

    # make the last one as 0 is the destination
    dp[len_nums - 1] = 0

    # fill the dp array with the minimum count till from last to the beginning
    for i in range(len_nums - 2, -1, -1):
        for step in range(1, nums[i] + 1):
            # calculate the next position
            next_position = i + step

            if next_position < len_nums:
                # if next position value is inf skip that
                if math.isinf(dp[next_position]):
                    continue

                dp[i] = min(dp[i], dp[next_position]+1)

    print(dp)



if __name__ == '__main__':
    jump([2, 3, 1, 1, 4])
