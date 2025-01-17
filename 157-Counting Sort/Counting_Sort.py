def counting_sort(arr):
    # find the maximum value of the array
    max_num = max(arr)

    # make the counting arry
    count_arr = [0] * (max_num + 1)

    # fill the counting array
    for i in arr:
        count_arr[i] += 1
    
    # rebuild the array
    sorted_arr = []
    for i in range(len(count_arr)):
        sorted_arr.extend([i] * count_arr[i])

    return sorted_arr

if __name__ == "__main__":

    # call the function
    arr = [4, 2, 2, 8, 3, 3, 1]
    sorted_arr = counting_sort(arr)
    print(sorted_arr)