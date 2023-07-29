from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    df = defaultdict(list)
    op = s.count('(') + 1
    whole = s.count('()') 
    print(n - whole + 1)