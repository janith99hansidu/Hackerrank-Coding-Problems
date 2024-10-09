import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    # length of the row and column
    row_len = len(A)
    column_len = len(A[0])
    
    total_area = 0
    
    # Traverse row wise
    for r in range(row_len):
        for c in range(column_len):
            # Top and bottom surfaces
            total_area += 2 
            
            # Check the neighboring cells to compute the sides
            # Left neighbor
            if c == 0:
                total_area += A[r][c]  
            else:
                total_area += max(0, A[r][c] - A[r][c-1])  

            # Right neighbor
            if c == column_len - 1:
                total_area += A[r][c] 
            else:
                total_area += max(0, A[r][c] - A[r][c+1])

            # Front neighbor
            if r == 0:
                total_area += A[r][c] 
            else:
                total_area += max(0, A[r][c] - A[r-1][c]) 

            # Back neighbor
            if r == row_len - 1:
                total_area += A[r][c] 
            else:
                total_area += max(0, A[r][c] - A[r+1][c])

    return total_area


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    print(result)
