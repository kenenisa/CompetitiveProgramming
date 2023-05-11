from collections import defaultdict 
# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = list(map(int,input().split()))
group_a = defaultdict(list)
for k in range(n):
    group_a[input()].append(str(k+1))
for i in range(m):
    found = group_a[input()]
    if found:
       print(" ".join(found))
    else:
        print("-1")
