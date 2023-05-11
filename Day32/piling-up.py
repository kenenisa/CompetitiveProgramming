# Enter your code here. Read input from STDIN. Print output to STDOUT
test = int(input())
for _ in range(test):
    n = int(input())
    blocks = list(map(int,input().split()))
    left = 0
    right = n - 1
    topOfThePile = max(blocks[left],blocks[right]) 
    valid = True
    while left < right and valid:
        if blocks[left] > blocks[right]:
            if topOfThePile >= blocks[left]:
                topOfThePile = blocks[left]
                left += 1
            else:
                valid = False
        if blocks[left] <= blocks[right]:
            if topOfThePile >= blocks[right]:
                topOfThePile = blocks[right]
                right -= 1
            else:
                valid = False
        
    print("Yes" if valid else "No")