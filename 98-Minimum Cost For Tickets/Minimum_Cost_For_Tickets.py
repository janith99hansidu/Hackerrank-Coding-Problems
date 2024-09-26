def minimumCost(arr, costs):
    # Base case: if the array is empty, no more cost is needed
    if not arr:
        return 0

    # Find the next array after using a 1-day pass
    next_one_arr = arr[1:]

    # Find the next array after using a 7-day pass
    i = 0
    while i < len(arr) and arr[i] <= arr[0] + 6:
        i += 1
    next_seven_arr = arr[i:]

    # Find the next array after using a 30-day pass
    i = 0
    while i < len(arr) and arr[i] <= arr[0] + 29:
        i += 1
    next_thirty_arr = arr[i:]

    # Calculate the minimum cost by comparing the cost of 1-day, 7-day, and 30-day passes
    current_cost = min(
        costs[0] + minimumCost(next_one_arr, costs),  # 1-day pass
        costs[1] + minimumCost(next_seven_arr, costs),  # 7-day pass
        costs[2] + minimumCost(next_thirty_arr, costs)  # 30-day pass
    )

    return current_cost


if __name__ == '__main__':
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]

    print(minimumCost(days, costs))
