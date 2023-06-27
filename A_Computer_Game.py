t = int(input())
for _ in range(t):
    n = int(input()) - 1
    a = input()
    b = input()
    def run():
        for i in range(n):
            if a[i] != "0" and b[i] != "0":
                return "NO"
        return "YES"



    print(run())
