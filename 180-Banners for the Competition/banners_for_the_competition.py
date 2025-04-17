def banners(s: str, p:str):
    # if the length is mismatch return -1
    if len(s) != len(p):
        return -1
    
    # store the total distance
    total = 0

    # calculate the distance
    for i in range(len(s)):
        # convert to ascii value and get the difference
        diff = abs(ord(s[i]) - ord(p[i]))
        # check whether the diff is more than half
        if diff > 13:
            # if larger than 13 we should consider backward
            diff = 26 - diff
            # calculate the total
            total += diff
        else:
            total += diff
    
    # return the calculated value
    return total
    
if __name__ == "__main__":
    # get the inputs
    total = banners("code", "hack")
    print(total)