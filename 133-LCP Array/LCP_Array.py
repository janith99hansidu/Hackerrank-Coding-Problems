def suffix_array_construction(s):
    # make suffix array from a string
    n = len(s)
    suffixes = sorted((s[i:],i) for i in range(n))
    suffix_arr = [suffix[1] for suffix in suffixes]
    
    return suffix_arr

def lcp_array_construction(s, suffix_arr):
    # rank array means given suffix the position where the suffix is located
    n = len(s)
    rank = [0] * n
    lcp = [0] * (n - 1)
    
    # traverse the suffix array and fill what is the rank of i suffix
    for i, suffix in enumerate(suffix_arr):
        rank[suffix] = i
    
    h = 0
    # build the lcp array 
    for i in range(n):
        # do not fill the first element in the rank array 
        if rank[i] > 0:
            # get the previous element to comparison 
            j = suffix_arr[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            # update the lcp array
            lcp[rank[i] - 1] = h
            # optimization to recalculate 
            if h > 0:
                h -= 1
    
    return lcp
    
if __name__ == "__main__":
    # sample usage of lcp
    suffix_arr = suffix_array_construction("banana")
    lcp = lcp_array_construction("banana", suffix_arr)
    print(lcp)