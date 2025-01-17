def couting_sort_for_radix(arr, exp):
    # initialize the variables
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # count the occerences of each digit
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    # update the count positions with actual values
    for i in range(1, 10):
        count[i] += count[i-1]
    
    # then traverse from the last index of the given arry
    # get the position by substracting the count arry value
    i = n - 1
    while i >= 0:
        # get the index of the current value in array 
        index = (arr[i] // 10) % 10
        # get the count - 1 value that is the position 
        output[count[index] - 1] = arr[i]
        # update the count[index] value 
        count[index] -= 1
        i -= 1
    
    # copy to the arr back
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # find the maximum number of given
    max_num = max(arr)
    exp = 1

    # loop through each digit of the array
    while max_num // exp > 0:
        couting_sort_for_radix(arr, exp)
        exp *= 10


if __name__ == "__main__":
    # example
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    radix_sort(arr)