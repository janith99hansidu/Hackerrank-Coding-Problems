# brute force method
def pairs(k, arr):
    # make a list of unique values set
    arr_set = set(arr)
    count = 0
    
    for num in arr:
        # checking num + k in the list get average o(1) time complexity 
        if (num + k) in arr_set:
            count += 1
        # checking num + k in the list get average o(1) time complexity
        if (num - k) in arr_set:
            count += 1
    
    return count // 2

if __name__ == '__main__':
    print(pairs(2, [1, 5, 3]))