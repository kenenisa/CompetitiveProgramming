t = int(input())
for _ in range(t):
    n,k=list(map(int,input().split()))
    s = input()
    i = 0
    result = 0
    while i < n:
        if s[i] =="B":
            result += 1
            i += k
            continue
        i+=1
    print(result)
