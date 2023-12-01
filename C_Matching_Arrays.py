def run():
    n,x=list(map(int,input().split()))
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a = list(zip(a,range(n)))
    a.sort(reverse=True)
    b.sort()
    result = [0]*n
    # match
    j = 0
    for i in range(x-1,-1,-1):
        if b[i] >= a[j][0]:
            return "NO"
        result[a[j][1]] = b[i]
        j+=1
    # un-match
    for i in range(n-1,x-1,-1):
        if b[i] < a[j][0]:
            return "NO"
        result[a[j][1]] = b[i]
        j+=1
    print("YES")
    return " ".join(map(str,result))


t = int(input())
for _ in range(t):
    print(run())   