def subsets(nums):
    result = []
    
    def backtrack(start, path):
        # 1. add a copy of the path
        result.append(path[:])
        
        # 2. from the start till the end of the nums 
        # add element and remove from that from the path 
        for i in range(start, len(nums)):
            # path append the next element
            path.append(nums[i])
            # call the function backtrack 
            backtrack(i+1, path)
            # remove last add element form the path
            path.pop()
        
    backtrack(0, [])
    return result


if __name__ == "__main__":
    print(subsets([1,2,3]))
        