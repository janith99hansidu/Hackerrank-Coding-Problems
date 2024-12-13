from collections import Counter

def isValid(s):
    # count the number of occurrences 
    char_count = Counter(s)
    # print(char_count)
    
    # count frequencies of each 
    # there is 2 possible to the condition for correct
    # if the larger frequency count is more than one from the lower one
    # if the lower frequency one occur only once
    freq_count = Counter(char_count.values())
    
    if len(freq_count) == 1:
        # all characters have the same frequency
        return "YES"
    elif len(freq_count) == 2:
        # make the conditions otherwise return NO
        freq_1, count_1 = freq_count.most_common()[0]
        freq_2, count_2 = freq_count.most_common()[1]
        
        # if there is only one element in with count 1
        if (freq_1 == 1 and count_1 == 1) or (freq_2 == 1 and count_2 == 1):
            return "YES"
        # check if we can remove one occurrence of the higher frequency
        elif abs(freq_1 - freq_2) == 1 and (count_1 == 1 or count_2 == 1):
            return "YES"
        
    return "NO"
    
if __name__ == '__main__':
    
    s = input()
    result = isValid(s)
    print(result)