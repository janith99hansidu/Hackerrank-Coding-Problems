def highestValuePalindrome(s, n, k):
    # convert to a list
    s_list = list(s)
    # check how many letters have to change for make it palindrome
    mid_index = n // 2
    changed = [False] * n

    # step 1 : make it palindrome
    for i in range(mid_index):
        if s_list[i] != s_list[n - i - 1]:
            # change smaller to larger
            s_list[i] = s_list[n - i - 1] = max(s_list[i], s_list[n - i - 1])
            changed[i] = True
            k -= 1

    # if change more than allowed
    if k < 0:
        return "-1"

    # step 2 : we change the string once to make it palindrome
    # if there is more k change them to "9" to maximize
    for i in range(n // 2):
        if k <= 0:
            break
        if s_list[i] != '9':
            # If we already changed this pair, we need 1 more change to make both 9
            if changed[i]:
                s_list[i] = s_list[n - i - 1] = '9'
                k -= 1
            # If the pair was not changed yet, we need 2 changes to make both 9
            elif k >= 2:
                s_list[i] = s_list[n - i - 1] = '9'
                k -= 2

    # change the middle value
    if k > 0 and n % 2 == 1:
        s_list[mid_index] = '9'

    return ''.join(s_list)


if __name__ == '__main__':
    print(highestValuePalindrome('092282', 6, 3))
    print(highestValuePalindrome('0011', 4, 1))

