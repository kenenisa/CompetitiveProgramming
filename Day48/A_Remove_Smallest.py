t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    def findSpace():
        for i in range(n-1):
            if a[i+1] - a[i] > 1:
                return "NO"
        return "YES"
    print(findSpace())