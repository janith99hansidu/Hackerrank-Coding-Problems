# recursion + memorization
def findLongestPalindrome(X, i, j, lookup):
    # if the i < j that means left pointer go than right pointer
    if i > j:
        return 0

    # if i == j means one letter
    if i == j:
        return 1

    key = (i, j)

    if key not in lookup:
        # if X[i] == X[j] means get a palindrome so check for the others
        if X[i] == X[j]:
            lookup[key] = findLongestPalindrome(X, i + 1, j - 1, lookup) + 2
        else:
            # if it doesn't match a letter find max of all possible string methods
            lookup[key] = max(findLongestPalindrome(X, i, j - 1, lookup), findLongestPalindrome(X, i + 1, j, lookup))

    return lookup[key]


if __name__ == '__main__':
    X = 'ABBDCACB'
    n = len(X)

    lookup = {}
    print('The length of the longest palindromic subsequence is',
          findLongestPalindrome(X, 0, n - 1, lookup))
