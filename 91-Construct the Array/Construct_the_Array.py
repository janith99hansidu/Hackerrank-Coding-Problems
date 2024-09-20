MOD = 10 ** 9 + 7


def countArray(n, k, x):
    # make a array to store that are ending with the x and not ending with the x
    ending_x = [0] * n
    not_ending_x = [0] * n

    # initialize the array
    not_ending_x[0] = 1
    for i in range(1, n):
        # ending with x is same as not ending with previous state
        ending_x[i] = not_ending_x[i - 1]

        # calculate the not ending with the element
        not_ending_x[i] = ending_x[i - 1] * (k - 1) + not_ending_x[i - 1] * (k - 2)

    return ending_x[n - 1]


if __name__ == '__main__':
    countArray(4, 3, 2)
