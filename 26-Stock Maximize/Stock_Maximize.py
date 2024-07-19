def stockmax(prices):
    # make the relevant variable
    n = len(prices)
    global_maximum = prices[n - 1]
    profit = 0

    # traverse through the prices in the array
    for i in range(n - 2, -1, -1):
        if global_maximum > prices[i]:
            profit = profit + (global_maximum - prices[i])
        else:
            global_maximum = prices[i]

    return profit


if __name__ == '__main__':
    stockmax([1, 3, 1, 2])
    stockmax([1, 2, 100])
