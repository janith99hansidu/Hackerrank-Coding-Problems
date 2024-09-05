def highestValuePalindrome(s, n, k):
    # convert to a list
    s_list = list(s)
    # check how many letters have to change for make it palindrome
    mid_index = (n + 1) // 2
    need_change = 0

    for i in range(mid_index):
        if s_list[i] != s_list[n - i - 1]:
            need_change += 1

    # start from the middle and traverse through the end
    for i in range(mid_index, -1, -1):

        # if k < 0 return -1
        if k <= 0:
            return '-1'

        # if the strings are not equal
        if s_list[i] != s_list[n - i - 1]:

            # check whether k >= than need_change*2
            # then we can change the letter by 2
            if k >= need_change * 2:
                # change the index by 2
                s_list[i] = s_list[n - i - 1] = str(9)

                # change the variables
                need_change -= 1
                k -= 2
            else:
                max_elem = max(s_list[i], s_list[n - i - 1])
                s_list[i] = s_list[n - i - 1] = str(max_elem)

                # change the variables
                need_change -= 1
                k -= 1

    # change the middle value
    if k > 0 and n % 2 == 1:
        s_list[mid_index - 1] = '9'

    return ''.join(s_list)


if __name__ == '__main__':
    print(highestValuePalindrome('092282', 6, 3))
    print(highestValuePalindrome('0011', 4, 1))

