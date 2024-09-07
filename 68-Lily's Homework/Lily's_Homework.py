def lilysHomework(arr):
    # Write your code here
    def count_swaps(sorted_arr):
        # variables
        swaps = 0  # number of swaps that need to make it sorted
        index_dict = {value:index for index,value in enumerate(arr)}  # map the value and index in given array
        arr_copy = arr.copy()  # copy the array to make the change to the copied array

        for i in range(len(sorted_arr)):
            if sorted_arr[i] != arr_copy[i]:

                correct_value = sorted_arr[i]
                # find where is the correct value at the actual array
                swap_index = index_dict[correct_value]

                # change the index map to correct order
                index_dict[correct_value] = i
                index_dict[arr_copy[i]] = swap_index

                arr_copy[i], arr_copy[swap_index] = arr_copy[swap_index], arr_copy[i]

                # increment the swap count
                swaps += 1

        return swaps

    asc_arr = sorted(arr)
    dec_arr = sorted(arr,reverse=True)

    return min(count_swaps(asc_arr), count_swaps(dec_arr))

if __name__ == '__main__':
    # 3 4 2 5 1
    print(lilysHomework([3, 4, 2, 5, 1]))