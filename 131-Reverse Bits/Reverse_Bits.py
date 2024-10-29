def reverseBits(n):
    # 1. make a space to the last bit of the result
    # 2. extract the bit of n 
    # 3. shift right the n number
    reversed_num = 0
    for _ in range(32):
        # shift reversed sum to left make a position to next
        reversed_num <<= 1
        # add reversed sum to the last bit in the number
        reversed_num |= (n & 1)
        # shift right to get the next position in n
        n >>= 1
    
    return reversed_num
    
if __name__ == "__main__":
    
    # handle the inputs
    n = int(input().strip())
    print(reverseBits(n))