def almostSorted(arr):
    sorted_arr = sorted(arr)

    if sorted_arr == arr:
        return

    # make start and end index = -1
    start = end = 0
    check_end = False

    # traverse through array and find start and end positions
    for i in range(len(arr) - 1, 0, -1):
        # if find the start position check for the end
        if not check_end:
            if arr[i] < arr[i - 1]:
                start = i
                check_end = True
        # check for the end
        if check_end:
            if arr[i] > arr[i - 1]:
                end = i

    # if reverse the sting and check whether equal to the sorted arr
    reverse_arr = arr[:end] + list(reversed(arr[end:start + 1])) + arr[start + 1:]
    arr[start], arr[end] = arr[end], arr[start]

    if arr == sorted_arr:
        print("yes")
        print("swap", start + 1, end + 1)
    elif reverse_arr == sorted_arr:
        print("yes")
        print("reverse", end + 1, start + 1)
    else:
        print("no")


if __name__ == '__main__':
    almostSorted([1, 5, 4, 3, 2, 6])
