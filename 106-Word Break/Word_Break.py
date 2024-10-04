def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """

    def backprop(start, path):
        # End case of the recursion
        if start == len(s):
            return True

        # Recursively check for the matching elements
        for end in range(start + 1, len(s) + 1):
            s1 = s[start:end]

            if s1 in wordDict:
                if backprop(end, path + [s1]):
                    return True

        # Return False if no valid segmentations were found
        return False

    return backprop(0, [])  # Return the result of backprop


if __name__ == '__main__':
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(wordBreak(s, wordDict))  # This will print True
