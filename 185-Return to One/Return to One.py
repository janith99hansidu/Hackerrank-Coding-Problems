def returnToOne(num):
    current = num
    num_steps = 0
    
    # while the current until get to the one
    while True:
        # end case
        if current == 1:
            return num_steps
        
        # check the number is odd or even
        if current % 2 == 0:
            current = current / 2
        else:
            current = current * 3 + 1
        
        # increment the current steps
        num_steps += 1

# get the inputs 
if __name__ == "__main__":
    num_test_cases = int(input().strip())
    for _ in range(num_test_cases):
        x, y = input().strip().split(" ")
        
        # call to the function and return
        kapila = returnToOne(int(x))
        kalpa = returnToOne(int(y))

        if kapila < kalpa:
            print("kapila")
        elif kalpa < kapila:
            print('kalpa')
        else:
            print("-")

