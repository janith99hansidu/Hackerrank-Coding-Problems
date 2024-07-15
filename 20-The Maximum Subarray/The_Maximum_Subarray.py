def maxSubarray(arr):
    # Write your code here
    # Maximum subarray of the array
    current_max = global_max = arr[0]
    for i in range(1, len(arr)):
        current_max = max(arr[i], current_max+arr[i])
        if current_max > global_max:
            global_max = current_max

    # Maximum subsequence of the array
    # add all plus values if arr contains otherwise get the max of minus element
    max_subsequence = sum(n for n in arr if n > 0) # add all plus values
    if max_subsequence == 0:
        max_subsequence = max(arr)

    return [global_max,max_subsequence]


if __name__ == '__main__':
    print(maxSubarray([2, -1, 2, 3, 4, -5]))