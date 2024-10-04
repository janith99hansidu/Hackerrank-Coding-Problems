def minimumDeleteSum(s1, s2):
    
    len_s1 = len(s1)
    len_s2 = len(s2)
    
    # add memorization 
    memo = {}
    
    # make helper function to recursively 
    def dp(s1_start, s2_start):
        
        # if already the value in the memo
        if (s1_start, s2_start) in memo:
            return memo[(s1_start, s2_start)]
        
        # end codition if both have met the len of both strings
        if s1_start == len_s1 and s2_start == len_s2:
            return 0
        
        # if s1 of the string met his end 
        if s1_start == len_s1:
            return dp(s1_start,s2_start+1) + ord(s2[s2_start])
        
        # if s2 of the string met his end 
        if s2_start == len_s2:
            return dp(s1_start+1,s2_start) + ord(s1[s1_start])
        
        # else calculate the sum with deleting one from each
        if s1[s1_start] == s2[s2_start]:
            total = dp(s1_start+1,s2_start+1)
        else:
            total = min(dp(s1_start,s2_start+1)+ord(s2[s2_start]),
                        dp(s1_start+1,s2_start)+ord(s1[s1_start])
                        )
        
        # save the calculated value to the memo
        memo[(s1_start, s2_start)] = total
        
        return total
    
    return dp(0,0)
            
    
if __name__ == "__main__":
    s1 = "sea"
    s2 = "eat"
    print(minimumDeleteSum(s1, s2))