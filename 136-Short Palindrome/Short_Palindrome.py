def shortPalindrome(s):
    # Write your code here
    # offset letters to 0-25
    MOD = 1000000007
    offset = ord('a')
    # store seen element once (use for fill the pairs in the seen_double)
    seen = [0] * 26
    # store seen element in pair vice 
    seen_double = [[0] * 26 for _ in range(26)]
    # store seen element in triple vice
    seen_triple = [0] * 26

    results = 0
    # traverse letters one by one 
    # 1. check triple is available for that element if available update the result
    # 2. then see the letter form any triple
    # 3. then see the pairs and update the seen_triple
    # 4. then update each pair using seen elements 

    for letter in s:
        current_letter = ord(letter) - offset

        # 1.
        results = (results + seen_triple[current_letter]) % MOD

        # 2.
        # traverse column wise and add to the relevant triple 
        for i in range(26):
            seen_triple[i] = (seen_triple[i] + seen_double[i][current_letter]) % MOD

        # 3.
        # traverse all seen letters and update the double table
        for i in range(26):
            seen_double[i][current_letter] = (seen_double[i][current_letter] + seen[i]) % MOD

        # 4.
        # update the seen table
        seen[current_letter] = (seen[current_letter] + 1) % MOD

    return results

    
if __name__ == '__main__':

    s = input()

    result = shortPalindrome(s)
    
    print(result)