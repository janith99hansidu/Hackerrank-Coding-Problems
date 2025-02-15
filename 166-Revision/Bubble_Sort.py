# 1. get the array of element 
# 2. check for the adjacent element if the element are i > i+1 then swap with the element
# 3. do this for the util n-2 

def bubbleSort(arr):
    len_arr = len(arr)

    for i in range(len_arr-1,-1, -1):
        for j in range(i):
            # check for the swapping 
            # print(i,j)
            if arr[j] > arr[j+1]:
                # then swap
                # swap()
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    
    return arr

if __name__ == "__main__":
    print(bubbleSort([5,3,6]))