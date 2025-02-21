def findTargetSumWays(nums, target):
    # we can also save the state of the current value as memorization 
    # global variables of the given array
    len_nums = len(nums)

    # recursive function to call the 
    def current(i, total):
        # if the total = target and the numbers are over
        if total == target and i >= len_nums:
            return 1
        
        # if the numbers are over and not equal to the total
        if i >= len_nums:
            return 0
    
        # otherwise get a number and add the positive of the number and the negative of the number
        num_of_ways = current(i+1, total + ( -1 * nums[i])) + current(i+1, total + (1 * nums[i]))

        # return the num_of_ways
        return num_of_ways
    
    return current(0, 0)

if __name__ == "__main__":
    nums = [1,1,1,1,1]
    target = 3
    print(findTargetSumWays(nums, target))