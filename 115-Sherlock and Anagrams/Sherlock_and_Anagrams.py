from itertools import combinations
from collections import Counter

def sherlockAndAnagrams(s):
    
    # count the possible same string count
    anagram_count = 0
    # get each possible window sizes from 1 to len(string)
    for window_size in range(1, len(s)):
        
        # generate all possible substrings of the current window size
        substrings = [s[i:i+window_size] for i in range(len(s) - window_size + 1)]
        
        # generate all possible combinations of two substrings
        for combo in combinations(substrings, 2):
            if Counter(combo[0]) == Counter(combo[1]):
                anagram_count += 1
    
    return anagram_count
            
if __name__ == '__main__':
    # handle the inputs given
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = sherlockAndAnagrams(s)