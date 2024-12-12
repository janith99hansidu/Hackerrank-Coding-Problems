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
        

    
if __name__ == '__main__':
    
    s = input()
    result = isValid(s)
    print(result)