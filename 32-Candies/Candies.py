def candies(n, arr):
    increasing_l = [1] * n
    decreasing_l = [1] * n

    for i in range(1, n):
        # fill increasing l
        if arr[i] > arr[i - 1]:
            increasing_l[i] = increasing_l[i - 1] + 1

        # fill the decreasing l
        if arr[n - i] < arr[n - i - 1]:
            decreasing_l[n - i - 1] = decreasing_l[n - i] + 1

    total = 0
    # add the maximum values of each
    for i in range(n):
        total = total + max(increasing_l[i], decreasing_l[i])

    return total


if __name__ == '__main__':
    print(candies(10, [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]))
