def subsets(nums):
    result = []
    n = len(nums)
    
    # 1. make a bit mask range 
    for i in range(1 << n):
        subset = []
        # 2. shift one bit from n and get the num
        for j in range(n):
            if i & (1 << j):    
                subset.append(nums[j])
        result.append(subset)
    
    return result
    
if __name__ == "__main__":
    print(subsets([1,2,3]))