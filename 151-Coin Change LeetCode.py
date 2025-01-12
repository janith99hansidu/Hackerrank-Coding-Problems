def coinChange(coins, amount):
    # initialize dp array
    dp = [float('inf')] * (amount + 1)
    
    # base case
    dp[0] = 0
    
    # fill the dp array
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == "__main__":
    coins = [1,2,5]
    amount = 11
    
    print(coinChange(coins, amount))
    coins = [2]
    amount = 3
    
    coinChange(coins, amount)
    
        
    