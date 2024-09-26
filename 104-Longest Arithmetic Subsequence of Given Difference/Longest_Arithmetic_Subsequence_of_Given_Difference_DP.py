def longestSubsequence(arr, difference):
    n = len(arr)
    # Initialize n_arr where each element is 1 (each element itself is a subsequence of length 1)
    n_arr = [1] * n

    # Dictionary to store the last position of each number
    num_dict = {}

    # Variable to keep track of the maximum length of subsequence
    max_length = 1

    # Traverse the array in reverse order
    for i in range(n - 1, -1, -1):
        num = arr[i]

        # Check if the current number + difference exists in num_dict (i.e., at some future position)
        if num + difference in num_dict:
            # Update n_arr[i] based on the position of num + difference
            next_position = num_dict[num + difference]
            n_arr[i] = n_arr[next_position] + 1

        # Update the dictionary with the current number and its position
        num_dict[num] = i

        # Update the maximum length found so far
        max_length = max(max_length, n_arr[i])

    return max_length


if __name__ == '__main__':
    arr = [1, 5, 7, 8, 5, 3, 4, 2, 1]
    difference = -2

    print(longestSubsequence(arr, difference))
