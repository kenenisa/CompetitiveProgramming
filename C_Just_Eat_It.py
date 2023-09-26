t = int(input())
for _ in range(t):
    def run():
        n = int(input())
        a = list(map(int,input().split()))
        s = sum(a)
        result = True
        part = 0
        for i in range(n-1):
            part += a[i]
            if part >= s or part <= 0:
                return "NO"
        return "YES"
    print(run())