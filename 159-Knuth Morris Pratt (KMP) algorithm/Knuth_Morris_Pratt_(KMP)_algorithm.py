def kmp_search(text, pattern):

    # pre compute the lps array
    def compute_lps_array(pattern):
        # initialize the variables
        len_pattern = len(pattern)
        arr = [0] * len_pattern
        j = 0
        i = 1

        # traverse till i meet the end of the string
        while i < len_pattern:
            # check whether the i and j are match
            if pattern[i] == pattern[j]:
                j += 1  # it is same when increment j or the value of the j + 1
                arr[i] = j
                i += 1
            else:
                if j != 0:
                    # go to the previous position value index
                    j = arr[j - 1]
                else:
                    arr[i] = 0
                    i += 1
        
        return arr
    
    # calculate the lps array
    lps_arr = compute_lps_array(pattern)
    len_pattern = len(pattern)
    len_text = len(text)

    # do the substring matching
    text_idx = 0 
    pattern_idx = 0

    while text_idx < len_text:
        # if the idx values are matching
        if text[text_idx] == pattern[pattern_idx]:
            text_idx += 1
            pattern_idx += 1
        
        # then check whether the pattern idx comes to the end
        if pattern_idx == len_pattern:
            # found the pattern
            print(f"Pattern found at index {text_idx - pattern_idx}")
            pattern_idx = lps_arr[pattern_idx - 1]
        elif text_idx < len_text and text[text_idx] != pattern[pattern_idx]:
            # mismatch after pattern_idx matches
            if pattern_idx != 0:
                pattern_idx = lps_arr[pattern_idx - 1]
            else:
                text_idx += 1

if __name__ == "__main__":
    # sample input 
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    kmp_search(text, pattern)
