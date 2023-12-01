from collections import defaultdict,deque, Counter
t = int(input())
for _ in range(t):
    n,k=list(map(int,input().split()))
    s = input()
    count = Counter(s)
    if k == count["B"]:
        print(0)
        continue
    elif k > count["B"]:
        x = count["B"]
        j = 0
        while x != k:
            if s[j] == "A":
                x += 1
            j+=1
        print(1)
        print(j,"B")
    else:
        x = count["B"]
        j = 0
        while x != k:
            if s[j] == "B":
                x -= 1
            j+=1
        print(1)
        print(j,"A")
