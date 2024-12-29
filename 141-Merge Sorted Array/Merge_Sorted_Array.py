def merge(nums1, m, nums2, n):
    # create a copy of the array
    nums1_copy = nums1.copy()
    # create variables for pointers of two arrays
    nums1_pointer = nums2_pointer = 0
    
    # both arrays are can be comparable
    while nums1_pointer < m and nums2_pointer < n:
        # check what number is larger and update the num1
        if nums1_copy[nums1_pointer] > nums2[nums2_pointer]:
            # nums2 element is the smaller one
            nums1[nums1_pointer + nums2_pointer] = nums2[nums2_pointer]
            nums2_pointer += 1  
        else:
            nums1[nums1_pointer + nums2_pointer] = nums1_copy[nums1_pointer]
            nums1_pointer +=1
    
    # if one array is over 
    # check what array is over and fill the remaining elements to the array 
    if nums1_pointer < m:
        # nums1 array is not over 
        while nums1_pointer < m:
           nums1[nums1_pointer + nums2_pointer] = nums1_copy[nums1_pointer]
           nums1_pointer += 1 
    else:
        # nums2 array is not over
        while nums2_pointer < n:
           nums1[nums1_pointer + nums2_pointer] = nums2[nums2_pointer]
           nums2_pointer += 1 
    
    
if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    print(nums1)