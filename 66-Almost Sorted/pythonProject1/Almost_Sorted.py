def almostSorted(arr):
    sorted_arr = sorted(arr)

    if sorted_arr == arr:
        print("yes")
        return

    start = end = -1

    # Traverse through the array to find start and end positions
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            start = i
            break

    for i in range(len(arr) - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            end = i
            break

    # Attempt to swap
    arr[start], arr[end] = arr[end], arr[start]

    if arr == sorted_arr:
        print("yes")
        print("swap", start + 1, end + 1)
    else:
        # Revert swap and attempt reverse
        arr[start], arr[end] = arr[end], arr[start]
        reverse_arr = arr[:start] + list(reversed(arr[start:end + 1])) + arr[end + 1:]

        if reverse_arr == sorted_arr:
            print("yes")
            print("reverse", start + 1, end + 1)
        else:
            print("no")


if __name__ == '__main__':
    almostSorted([1, 5, 4, 3, 2, 6])
