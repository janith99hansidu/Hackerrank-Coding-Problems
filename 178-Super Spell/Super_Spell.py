def super_spell(arr_strings: list):
    # at first get the smallest possible 
    # each new string came get the last more than last character smallest value
    # greedy search
    # this is current string minimum 
    prev_string_min = 0
    
    # add a character for each string
    total_string = []

    for string_val in arr_strings:

        # get the minimum of current string
        current_string_min = string_val[0]

        for i in range(1, len(string_val)):
            
            # check whether the string is smaller than current min 
            # check for the smallest value
            if (ord(current_string_min) >= ord(string_val[i])) and (prev_string_min <= ord(string_val[i])):
                # so make as current min
                current_string_min = string_val[i]

        # add to the total string the minimum 
        total_string.append(current_string_min)
        prev_string_min = ord(current_string_min)
    
    print(''.join(total_string))

if __name__ == "__main__":
    arr_strings = ['asdfsdf','sdfsdfb','sfsdfd']
    super_spell(arr_strings)
    arr_strings = ['xyztxc', 'pqurstwxe']
    super_spell(arr_strings)