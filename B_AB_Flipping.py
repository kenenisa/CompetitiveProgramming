t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())
    
    b = 0
    seenB = False
    result = 0
    i = n-1
    while i >= 0:
        if s[i] == "B":
            b+=1
        else:
            result += b
            if b > 0:
                s[i] = "B"
                b = 0
                continue
        i-=1
    print(result)