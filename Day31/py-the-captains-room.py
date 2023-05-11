# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
d = defaultdict(int)

n = int(input())
rooms = list(map(int,input().split()))
for i in rooms:
    d[i] += 1
    
print(sorted(d.items(),key= lambda i:i[1])[0][0])
