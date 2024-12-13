# make frequency dictionary from given substring
# divide the all numbers from 2 to get pairs of strings
# modulo operator to get all remaining not pair elements
# calculate the maximum palindromes using mathematics
# ordering and nPr from maths

def answerQuery(l, r):
    # Return the answer for this query modulo 1000000007.

if __name__ == '__main__':

    s = input()

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(l, r)