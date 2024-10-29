# bit manipulation 
def isPowerOfTwo(n):
    
    if n < 0:
        return 'false'
    if (n & (n - 1) == 0):
        return 'true'
    else:
        return 'false'       

if __name__ == "__main__":
    
    # handle the input 
    
    n = int(input())
    print(isPowerOfTwo(n))