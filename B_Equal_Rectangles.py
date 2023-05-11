t = int(input())
for _ in range(t):
    def run():
        n = int(input())
        a = list(map(int,input().split()))
        a.sort()
        if a[0] != a[1] or a[-1] != a[-2]:
            return "NO"
        area = a[0] * a[-1]
        for i in range(2,len(a)//2,2):
            if a[i]!= a[i+1] or a[-i-1] != a[-i-2] or a[i] * a[-i-1] != area:
                return "NO"
        return "YES"
    print(run())
    