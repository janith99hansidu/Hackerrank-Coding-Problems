def maxMin(k, arr):
    # Write your code here
    sorted_arr = sorted(arr)
    len_arr = len(arr)
    min_num = sorted_arr[k-1] - sorted_arr[0]

    for i in range(1, len_arr - k + 1):
        current_min = sorted_arr[i + k - 1] - sorted_arr[i]
        if current_min < min_num:
            min_num = current_min

    return min_num


if __name__ == '__main__':
    maxMin(4, [1, 2, 3, 4, 10, 20, 30, 40, 100, 200])
    maxMin(2, [1, 2, 1, 2, 1])
    maxMin(3,[10, 100, 300, 200, 1000, 20, 30])