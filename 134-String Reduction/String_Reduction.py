# Recursive solution high time complexity 
def stringReduction(s):
    given_set = {'a', 'b', 'c'}
    min_length = len(s)
    memo = {}
    
    def rec(s):
        
        nonlocal min_length
        # memorize the s
        if s in memo:
            return memo[s] 
        # if the current string s is smaller than min_lenth update it
        if len(s) < min_length:
            min_length = len(s)
            
        i = 0
        while i < len(s) - 1:
            
            # step 1: get the first 2 element check whether they are not similar
            if s[i] != s[i+1]:
                # step 2: do the change operation with the next element
                next_elem = (given_set - {s[i], s[i + 1]}).pop()
                # replace the string next two element with the next element
                new_s = s[:i] + next_elem + s[i+2:]
                # step 4: call to the function recursively
                rec(new_s)
            
            # increament the i value
            i += 1
        
        memo[s] = min_length
        return min_length
    
    rec(s)
    return min_length    
    
    
if __name__ == "__main__":
    # handle the inputs
    t = int(input().strip())

    for t_itr in range(t):
        s = input().strip()
        result = stringReduction(s)
        print(result)