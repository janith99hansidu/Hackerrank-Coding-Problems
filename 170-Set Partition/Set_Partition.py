def set_partition(s, k, subsets=None, index=0):
    # initially create given list as size of given set
    if subsets == None:
        # make given empty sets
        subsets = [[] for _ in range(k)]
    
    # check for the base condition 
    if index == len(s):
        if all(subsets):
            print(subsets)
        return
    
    # add the given index and remove them using pop go to next leaf
    for i in range(k): # add to the fist subset or other subset
        subsets[i].append(s[index])
        # call to the recursive fn to explore
        set_partition(s, k, subsets, index+1)
        # pop the last add element from the set to further explore
        subsets[i].pop()
    

if __name__ == "__main__":
    print(set_partition([1, 2, 3], 2))