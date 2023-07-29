t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    result = 1
    c = 1
    for i in range(1,n):
        if s[i] == s[i-1]:
            c += 1
        else:
            c = 1
        result = max(result,c)
    print(result+1)