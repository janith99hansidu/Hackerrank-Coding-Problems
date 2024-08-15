def minimumLoss(price):
    # prices_with_indices = [(p, i) for i, p in enumerate(price)]
    prices_indices = [(p, i) for i, p in enumerate(price)]
    prices_indices.sort()

    min_diff = float('inf')

    for i in range(len(prices_indices) - 1):
        first_num, first_index = prices_indices[i]
        second_num, second_index = prices_indices[i + 1]

        if (second_num - first_num < min_diff) & (second_index < first_index):
            min_diff = second_num - first_num

    return min_diff


if __name__ == '__main__':
    minimumLoss([20, 7, 8, 2, 5])
