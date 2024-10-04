import sys

def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """
    # sentences list of given string
    sentences = []
    def dp(start, current_list):
        
        # if the start is the len of the s 
        if start == len(s):
            sentences.append(" ".join(current_list))
            return
        
        # traverse from the start and get the possible ends
        for end in range(start+1, len(s)+1):
            if s[start:end] in wordDict:
                current_list.append(s[start:end])
                dp(end, current_list)
                current_list.pop()
        
        return
    
    dp(0,[])
    return sentences
        
if __name__ == "__main__":
    print(wordBreak("catsanddog",["cat","cats","and","sand","dog"]))
        

