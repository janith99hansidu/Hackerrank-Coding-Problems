def gridSearch(G, P):
    # Write your code here
    # get the rows and columns of the G
    row_g = len(G)
    column_g = len(G[0])
    row_p = len(P)
    column_p = len(P[0])
    # print(row_g,column_g,row_p,column_p)

    # if do not match
    do_not_match = False

    # How many steps can take in row and column
    step_row = row_g - row_p + 1
    step_column = column_g - column_p + 1

    # traverse to starting position in row G
    for i in range(step_row):
        for j in range(step_column):
            # reset the do_not_match flag
            do_not_match = False
            # traverse to starting position
            # traverse through the elements to check pattern match
            for k in range(row_p):
                if do_not_match:
                    break
                for l in range(column_p):
                    # check the pattern match the G
                    if P[k][l] != G[i + k][l + j]:
                        do_not_match = True
                        break
                    else:
                        pass

            if not do_not_match:
                return "YES"

    return "NO"



if __name__ == '__main__':
    gridSearch(["1234567890",
                "0987654321",
                "1111111111",
                "1111111111",
                "2222222222"], ["876543",
                                "111111",
                                "111111"])
