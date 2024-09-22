def minCoins(coins, m, given_sum):
    # Initialize the dp array to store the minimum coins required for each sum
    dp = [float('inf')] * (given_sum + 1)

    # Base case: 0 coins are needed to make a sum of 0
    dp[0] = 0

    # Loop through all values from 1 to given_sum
    for i in range(1, given_sum + 1):
        # Check each coin
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[given_sum] is still float('inf'), it means the sum cannot be formed
    return dp[given_sum] if dp[given_sum] != float('inf') else -1


if __name__ == '__main__':
    coins = [5, 10, 25]
    m = len(coins)
    given_sum = 30

    print(minCoins(coins, m, given_sum))
