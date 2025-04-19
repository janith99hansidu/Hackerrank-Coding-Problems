# recursively find the possible other combinations
# that lead to zero
total_possibilities = [1*n for n in range(1,21)] + [2*n for n in range(1,21)] + [3*n for n in range(1,21)] + [25,50]
total_possibilities.sort()

def recursive_find(num):
    # end conditions
    if num == 0:
        return 1
    if num<0:
        return 0
    
    # initialize the sum 
    pos_sum = 0
    # get the all possible conditions
    for pos_val in total_possibilities:
        pos_sum += recursive_find(num-pos_val)
    
    return pos_sum

def dc(val):
    # first consider numbers with 2x till the number - 2x > 0 
    # then consider all number combinations
    # if the number is 0 end return 1 
    # if the number is < 0 return 0

    # step 1: find possibles that end with 2x ring
    possible_end_doubles = [2*n for n in range(1,21)] + [50]
    sum = 0
    for n in possible_end_doubles:
        if val - n > 0:
            sum += recursive_find(val - n) 
    
    # total possibilities
    return sum

if __name__ == "__main__":
    val = 4
    print(dc(val))
