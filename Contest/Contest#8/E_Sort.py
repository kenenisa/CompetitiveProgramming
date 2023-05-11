t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    def run():
        # check every even
        if n == 1:
            return "YES"
        for i in range(n-1,-1,-2):
            if i-1 > -1:
                if a[i-1] > a[i]:
                    a[i-1],a[i] = a[i],a[i-1]
        for i in range(1,n):
            if a[i-1] > a[i]:
                return "NO"
        return "YES"
    print(run())
