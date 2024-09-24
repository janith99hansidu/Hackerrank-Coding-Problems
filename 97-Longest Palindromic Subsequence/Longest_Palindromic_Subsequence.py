# recursion + memorization
def findLongestPalindrome(X, i, j):
    # if the i < j that means left pointer go than right pointer
    if i > j:
        return 0

    # if i == j means one letter
    if i == j:
        return 1

    # if X[i] == X[j] means get a palindrome so check for the others
    if X[i] == X[j]:
        return findLongestPalindrome(X, i + 1, j - 1) + 2

    # if it doesn't match a letter find max of all possible string methods
    return max(findLongestPalindrome(X, i, j - 1), findLongestPalindrome(X, i + 1, j))


if __name__ == '__main__':
    X = 'ABBDCACB'
    n = len(X)

    print('The length of the longest palindromic subsequence is',
          findLongestPalindrome(X, 0, n - 1))
