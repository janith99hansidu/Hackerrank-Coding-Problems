import math


def numSquares(n):

    # store the calculated values
    memo = {}

    def helper(k):
        # base case if the value is 0
        if k == 0:
            return 0

        # if the k is already calculated return that value
        if k in memo:
            return memo[k]

        # initialize the minvalue to inf
        min_count = float('inf')

        for j in range(1, int(math.sqrt(k)) + 1):
            square = j * j
            # Recursively find the minimum squares for k - j^2
            min_count = min(min_count, helper(k - square) + 1)

        # update the table
        memo[k] = min_count

        return min_count

    return helper(n)


if __name__ == '__main__':
    print(numSquares(12))

