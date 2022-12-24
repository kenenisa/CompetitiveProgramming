# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = list(map(int,input().split()))
N = list(map(int,input().split()))
a = set(map(int,input().split()))
b = set(map(int,input().split()))
# count intersection for each set and find the diff
happiness = 0

for i in N:
    if i in a:
        happiness += 1
    if i in b:
        happiness -= 1        
print(happiness)