from collections import defaultdict, deque, Counter
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(len(set(a)) - n%2)
