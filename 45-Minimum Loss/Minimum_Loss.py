def minimumLoss(price):

    min_loss = float('inf')

    for i in range(len(price) - 1, 0, -1):
        for j in range(i - 1, -1, -1):

            if (price[j] > price[i]) & (price[j] - price[i] < min_loss):
                min_loss = price[j] - price[i]

    return min_loss


if __name__ == '__main__':
    minimumLoss([20, 7, 8, 2, 5])
