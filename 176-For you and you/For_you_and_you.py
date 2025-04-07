def candies(apples):
    # recursive function 
    def recursive(index, current_max, total):
        # end condition of the recursion
        if index == len(apples):
            return current_max
        
        # otherwise get the i th index or not get that index
        # update current max if the number divide by 3
        with_i_max = current_max
        with_i_total = total + apples[index]
        if with_i_total % 3 == 0:
            # change the current max to with i
            with_i_max = with_i_total
        
        # recursive call to the next values
        current_max = max(recursive(index+1,with_i_max, with_i_total), recursive(index+1, current_max, total))
        
        # return the current max calculated to above tree
        return current_max

    return recursive(0, 0, 0)

if __name__ == "__main__":
    total = int(input())
    apples = input().split()
    apples = [int(i) for i in apples]
    
    print(candies(apples))