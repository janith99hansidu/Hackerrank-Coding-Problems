def canPartition(nums):
    total_sum = sum(nums)

    # If the total sum is odd, it cannot be partitioned equally
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2

    # Memoization dictionary to store previously computed results
    memo = {}

    def helper(current_sum, start_pos):
        # If we reach the target sum, return True
        if current_sum == target:
            return True

        # If we exceed the target sum or run out of elements, return False
        if current_sum > target or start_pos >= len(nums):
            return False

        # Memoization check
        if (current_sum, start_pos) in memo:
            return memo[(current_sum, start_pos)]

        # Explore two possibilities: include nums[start_pos] in the subset or not
        can_partition = helper(current_sum + nums[start_pos], start_pos + 1) or helper(current_sum, start_pos + 1)

        # Memoize the result for this state
        memo[(current_sum, start_pos)] = can_partition
        return can_partition

    # Start recursion with an initial sum of 0 and starting at index 0
    return helper(0, 0)


if __name__ == '__main__':
    nums = [2, 2, 1, 1]

    print(canPartition(nums))
