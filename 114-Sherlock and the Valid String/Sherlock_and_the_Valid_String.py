from collections import Counter

def isValid(s):
    # count the frequency of each character
    char_count = Counter(s)
    
    # count the frequency of these frequencies
    freq_count = Counter(char_count.values())
    
    if len(freq_count) == 1:
        # all characters have the same frequency
        return "YES"
    elif len(freq_count) == 2:
        # there are two different frequencies
        freq1, count1 = freq_count.most_common()[0]  
        freq2, count2 = freq_count.most_common()[1] 
        
        # check if the difference is 1 and one occurs only once
        if (freq1 == 1 and count1 == 1) or (freq2 == 1 and count2 == 1):
            return "YES"
        # check if we can remove one occurrence of the higher frequency
        elif abs(freq1 - freq2) == 1 and (count1 == 1 or count2 == 1):
            return "YES"
    
    return "NO"

    
if __name__ == '__main__':
    
    s = input()
    result = isValid(s)
    print(result)