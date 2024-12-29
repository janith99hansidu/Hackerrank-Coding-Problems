def findDuplicate(nums):
    # traverse the array and if a key already exist that is the dublicate num
    num_list = set()
    
    for i in nums:
        if i in num_list:
            return i
        else:
            num_list.add(i)
        
        
        
if __name__ == "__main__":
    duplicate_num = findDuplicate([1,3,4,2,2])
    print(duplicate_num)