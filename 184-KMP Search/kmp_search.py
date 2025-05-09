def kmp_search(pattern, string):
    # length of the pattern and the string
    pattern_len = len(pattern)
    string_len = len(string)
    
    # pointer to the pattern and string
    pattern_p = 0
    string_p = 0
    
    # build the lps array
    lps = [0]* len(pattern)
    j=0
    for i in range(1,pattern_len):
        # if it match to the front of the string add 1 to the previous
        if pattern[j] == pattern[i]:
            # if the j and i match to the current 
            lps[i] = lps[i-1] + 1
            # increment the j value for get the next character
            j+=1
        else:
            j=0
    
    # search with build lps array 
    while string_p < string_len:
        # if the string pointer match to the pattern pointer
        if string[string_p] == pattern[pattern_p]:
            string_p += 1
            pattern_p += 1

            # if it comes to the end
            if pattern_p == pattern_len:
                return string_p - pattern_p
        else:
            # if the characters does not match
            if pattern_p != 0:
                pattern_p = lps[pattern_p-1]
            else:
                string_p +=1

if __name__ == "__main__":
    pattern = "abcabc"
    string = "abcadeabcabdabcabc"
    print(kmp_search(pattern,string))
