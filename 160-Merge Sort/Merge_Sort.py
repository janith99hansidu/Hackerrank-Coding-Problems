def merge_sort(arr):
    # only do the merge sort length > 0
    if len(arr) > 0:
        # find the mid value of the array 
        mid = len(arr)

        # divide base on the mid
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # sort based on the left and right
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge the arrys
        i = j = k = 0
        while i < len(arr) and j < len(arr):
            # check the array
            if left_arr[i] < right_arr[j]:
                # increment the arr 
                arr[k] = left_arr[i]
                i += 1 
            else:
                # increment the next value
                arr[k] = right_arr[j]
                j += 1
            
            k += 1
        
        # remaining elements merging to the arry
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1