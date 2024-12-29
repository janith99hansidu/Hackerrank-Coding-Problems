def compress(chars):
    # store the current group of the letter
    group = chars[0]
    # store the current size of the group
    current_size = 1
    
    # list of letters
    chars_copy = chars[:]
    char_list = list()
    
    for i in range(1, len(chars)):
        # check whether the current string is equal to the group
        # if match do not update the list only update the current size
        # if do not match update the list with group and group size if > 1 and 
        # update the value of the group and current size
        
        if chars_copy[i] == group:
            current_size += 1
        else:
            char_list.append(group)
            
            if current_size > 1:
                char_list.extend(str(current_size))

            current_size = 1
            group = chars_copy[i]
    
    # add the last group
    char_list.append(group)      
    if current_size > 1:
        char_list.extend(str(current_size))
    
    # replace the chars list with charlist
    len_char_list = len(char_list)
    chars[:] = char_list
    
    return len_char_list
    
    
if __name__ == "__main__":
    total = compress(["a","a","b","b","c","c","c"])
    print(total)