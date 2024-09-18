def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    n = len(height)

    # store the left max and right max to an array
    left_max = [0] * n
    right_max = [0] * n

    # calculate the max of given position
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])

    right_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])

    # calculate the filled water one by one
    water_trapped = 0
    for i in range(n):
        water_trapped += min(left_max[i], right_max[i]) - height[i]

    return water_trapped


if __name__ == '__main__':
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
