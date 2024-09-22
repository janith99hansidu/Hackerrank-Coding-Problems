import sys


def minCoins(coins, m, given_sum):
    # base case if the given_sum == 0 retun
    if given_sum == 0:
        return 0

    res = sys.maxsize
    # initialize the res to maximum value
    if given_sum < 0:
        return res

    # try every coin and check the result get the minimum value
    for i in range(m):
        if coins[i] <= given_sum:
            # recursive call to the next function
            sub_res = minCoins(coins, m, given_sum - coins[i])

            if sub_res != sys.maxsize and sub_res + 1 < res:
                res = sub_res + 1

    return res


if __name__ == '__main__':
    coins = [5, 10, 25]
    m = len(coins)
    given_sum = 30

    print(minCoins(coins, m, given_sum))
