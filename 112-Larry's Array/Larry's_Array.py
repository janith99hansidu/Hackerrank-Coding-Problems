# rotate the index is not in the correct position 
# if the target index is not the current index swapping is done 
# only check till n-3 last 2 indexes should be align after that 
# if not in correct order that is incorrect 

# 1. swap based on one element 
def bubble_swap(numbers, current_idx, target_idx):
    # calculate number of swaps by two numbers full swap
    # if we do a full swap 
    # number of full swaps calculated with current_idx - target_idx because every time
    # position is reduced by 2
    num_full_swaps = (current_idx - target_idx) // 2
    
    # swap the element with number of calculated time
    for i in range(num_full_swaps):
        # current position of the number
        current_pos_idx = current_idx - 2*i
        
        # do the swapping 
        temp = numbers[current_pos_idx]
        numbers[current_pos_idx] = numbers[current_pos_idx - 1]
        numbers[current_pos_idx - 1] = numbers[current_pos_idx - 2]
        numbers[current_pos_idx - 2] = temp
        
    # if there is one element to be swapped
    current_pos_idx = current_idx - 2 * num_full_swaps
    remaining_idx = current_pos_idx - target_idx
    
    if remaining_idx == 1:
        # if there is one position to be swapped swap that element
        temp = numbers[current_pos_idx]
        numbers[current_pos_idx] = numbers[current_pos_idx + 1]
        numbers[current_pos_idx + 1] = numbers[current_pos_idx - 1]
        numbers[current_pos_idx - 1] = temp        

        
    
def larrysArray(A):
    # test bubble_swap function 
    # bubble_swap(A, 6, 1)
    # print(A)
    
    # do the bubble_swap for each util the n-2
    for i in range(1, len(A) - 2):
        # if the number of the i-1 position doesn't match to the i
        # do the swapping
        if A[i - 1] != i:
            bubble_swap(A, A.index(i), i - 1)
    
    # Check the condition for the last three numbers
    a, b, c = A[-3], A[-2], A[-1]
    if (a < b < c) or (b < c < a) or (c < a < b):
        return "YES"
    return "NO"
     
if __name__ == '__main__':
    
    # get the inputs
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)
        print(result)
    