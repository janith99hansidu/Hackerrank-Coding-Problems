# 7/23 are get correct from hackerrank
def highestValuePalindrome(s, n, k):
    # Write your code here
    # Check weather odd number or even number
    odd = n % 2 != 0
    s = list(s)

    # Traverse from the beginning and the end
    left = 0
    right = n - 1
    while left < right:
        if k <= 0:
            return -1
        elif s[left] != s[right]:
            max_num = max(s[left], s[right])
            s[left] = max_num
            s[right] = max_num

            # Update the left and right positions
            right = right - 1
            left = left + 1
            k = k - 1
            # print(s, k)
        else:
            right = right - 1
            left = left + 1

    # print(left,right,k)
    # check for the remaining
    if left == right and k == 1:
        s[left] = '9'
    else:
        left = 0
        right = len(s) - 1

        while left < right and k >= 2:
            # print(left,right)
            s[left] = '9'
            s[right] = '9'

            left = left + 1
            right = right - 1
            k = k - 2
            # print(s)
    result = ''.join(s)
    return result

if __name__ == '__main__':
    print(highestValuePalindrome("1231", 4, 5))
