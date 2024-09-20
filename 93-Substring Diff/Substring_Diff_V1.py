# substringDiff V1
# high time complexity
def substringDiff(k, s1, s2):
    # Write your code here
    len_s1 = len(s1)
    len_s2 = len(s2)

    # maximum number of changes
    max_substring_diff = -float('inf')

    # maek a dp array to keep track
    # columns are s2
    # rows are s1
    dp = [[0] * len_s2 for _ in range(len_s1)]

    # fill the dp table with sliding window and update the table
    for row in range(1, len_s1):
        for column in range(1, len_s2):

            current_row = row
            current_col = column
            current_k = k
            current_max = 0

            while current_row < len_s1 and current_col < len_s2:
                if s1[current_row-1] == s2[current_col-1]:
                    current_max += 1
                elif current_k > 0:
                    current_max += 1
                    # decrease the k
                    current_k -= 1

                # update the dp tabel by current max
                dp[current_row][current_col] = current_max

                # go to the next by diagonal
                current_row += 1
                current_col += 1

            if max_substring_diff < current_max:
                max_substring_diff = current_max

    return max_substring_diff


if __name__ == '__main__':
    print(substringDiff(2, "tabriz", "torino"))
    print(substringDiff(3,  "helloworld", "yellomarin"))