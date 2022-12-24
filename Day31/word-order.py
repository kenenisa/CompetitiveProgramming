# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
d = defaultdict(int) # if an item that doesn't exist gets accessed it's 0
n = int(input())
for _ in range(n):
    word = input()
    d[word] += 1
print(len(d)) # unique words
for i in list(d):
    print(d[i],end=" ") # amount for each word