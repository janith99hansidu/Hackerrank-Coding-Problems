def lps(pattern):
    # calculate the lps for string matching 
    len_pattern = len(pattern)
    arr = [0] * (len_pattern)
    j = 0
    i = 1

    # while the i < len of the string match the substrings
    while i < len_pattern:
        # check wether the characters are matching 
        if pattern[j] == pattern[i]:
            # then increment the j value and the update arr
            j += 1
            arr[i] = j
            i += 1
        else:
            # check whether the j != 0 if yes go to the previous matching position to start
            # from that position to check the matching
            if j != 0:
                j = arr[j - 1]
            else:
                arr[i] = 0
                # go to the next i position to check
                i += 1
    
    return arr

