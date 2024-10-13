def larrysArray(A):

     
if __name__ == '__main__':
    
    # get the inputs
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)
        print(result)
    