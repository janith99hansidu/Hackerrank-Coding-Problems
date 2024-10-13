def hackerlandRadioTransmitters(x, k):
    # sort the array
    x.sort()
    
    # number of anttenas
    num_anttenas = 0
    
    pointer = 0
    while pointer < len(x):
        # get the next element 
        next_element = x[pointer]
        # position of anttena placement
        pos_anttena = pointer
        
        # get the maximum position that can place the anttena
        max_antenna = next_element + k
        
        # search for the maximum places that can place the anttena
        while pointer < len(x) and x[pointer] <= max_antenna:
            pos_anttena = pointer
            pointer += 1
        
        # after searching for the position place the anttena
        num_anttenas += 1
        
        # search the coverage
        coverage = x[pos_anttena] + k
        while pointer < len(x) and x[pointer] <= coverage :
            pointer += 1
            
    return num_anttenas
        

if __name__ == "__main__":
    
    # handle the inputs
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)