def maximumToys(prices, k):
    # Write your code here
    sorted_arr = sorted(prices)
    total_sum = 0
    num_toys = 0

    for i in range(len(sorted_arr)):
        if sorted_arr[i] + total_sum > k:
            break
        else:
            total_sum += sorted_arr[i]
            num_toys += 1

    return num_toys

if __name__ == '__main__':
    maximumToys([1, 12, 5, 111, 200, 1000, 10], 50)