
def longestDiverseString(a, b, c):
    """
    :type a: int
    :type b: int
    :type c: int
    :rtype: str
    """
    memo = {}
    
    def dp(a_rem, b_rem, c_rem, last_char, last_count):
        
        # if there is no more letters to add return empty string 
        if a_rem == 0 and b_rem == 0 and c_rem == 0:
            return ""
        
        # already calculated the in the memory
        if (a_rem, b_rem, c_rem, last_char, last_count) in memo:
            return memo[(a_rem, b_rem, c_rem, last_char, last_count)]
        
        # initialize longest string to ""
        longest_string = ""
        
        # with letter a add a and find the remaining letters 
        if a_rem > 0 and not(last_char == 'a' and last_count == 2):
            new_string = 'a' + dp(a_rem - 1, b_rem, c_rem, 'a', last_count + 1 if last_char == 'a' else 1)
            if len(new_string) > len(longest_string):
                longest_string = new_string
        
        # with letter b add b and find the remaining letters 
        if b_rem > 0 and not(last_char == 'b' and last_count == 2):
            new_string = 'b' + dp(a_rem, b_rem-1, c_rem, 'b', last_count + 1 if last_char == 'b' else 1)
            if len(new_string) > len(longest_string):
                longest_string = new_string
                
        # with letter a add a and find the remaining letters 
        if c_rem > 0 and not(last_char == 'c' and last_count == 2):
            new_string = 'c' + dp(a_rem, b_rem, c_rem-1, 'c', last_count + 1 if last_char == 'c' else 1)
            if len(new_string) > len(longest_string):
                longest_string = new_string
        
        # add them to memory 
        memo[(a_rem, b_rem, c_rem, last_char, last_count)] = longest_string
        
        return longest_string
    
    return dp(a,b,c,"",0)
        
    
    
if __name__ == "__main__":
    print(longestDiverseString(1,1,7))
