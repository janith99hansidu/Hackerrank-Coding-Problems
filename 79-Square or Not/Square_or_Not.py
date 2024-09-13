import math


def squareOrNot(s):
    len_string = len(s)  # length of the string
    sqrt_len = int(math.sqrt(len_string))  # square root of the length
    if len_string != sqrt_len ** 2:
        return "No"

    # traverse the matrix
    beautiful = True
    side_len = sqrt_len
    for row in range(side_len):
        if not beautiful:
            break
        for column in range(side_len):
            # calculate the position of the current element
            value_position = row * side_len + column
            num_value = s[value_position]

            # check for the edge cases of the matrix: first and last rows/columns
            if row == 0 or row == side_len - 1 or column == 0 or column == side_len - 1:
                if num_value != "1":
                    beautiful = False
                    break
            else:
                if num_value != "0":
                    beautiful = False
                    break

    return "Yes" if beautiful else "No"


if __name__ == '__main__':
    # Read number of test cases
    t = int(input().strip())

    # Loop through each test case
    results = []
    for _ in range(t):
        n = int(input().strip())  # Read the length of the string (unused here)
        s = input().strip()  # Read the string

        # Store the result for each test case
        results.append(squareOrNot(s))

    # Output all results
    print("\n".join(results))
