def change(amount, coins):
    # memory that save the remaining and the beginning coin of the table
    memo = {}  # (remaining , coin)

    def helper(remaining, index):

        # end case if remaining is 0 return 1 there is a one way
        if remaining == 0:
            return 1

        # if the index goes to end of the coin or remaining < 0 return 0
        if remaining < 0 or index == len(coins):
            return 0

        # check weather the remaining,index is already calculated
        if (remaining, index) in memo:
            return memo[(remaining, index)]

        # recursion call for include that element and exclude that element
        include = helper(remaining - coins[index], index)
        exclude = helper(remaining, index + 1)

        # update the table
        memo[(remaining, index)] = include + exclude

        # return the value to upward in recursion
        return memo[(remaining, index)]

    return helper(amount, 0)


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 4

    print(change(amount, coins))
