def getMinimumCost(k, c):
    sorted_array = sorted(c, reverse=True)
    cost = 0

    for i in range(len(c)):
        multiplier = (i // k) + 1
        cost += multiplier * sorted_array[i]

    return cost


if __name__ == '__main__':
    getMinimumCost(3, [2, 5, 6])
    getMinimumCost(3,[1, 3, 5, 7, 9])
