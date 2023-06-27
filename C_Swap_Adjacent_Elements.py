n = int(input())
a = list(map(int, input().split()))
s = input()


def run():
    m = 0
    for i in range(n-1):
        m = max(m, a[i])
        if s[i] == "0" and m > i + 1:
            return "NO"
    return "YES"


print(run())