t = int(input())
name = [a for a in "Timur"]
name.sort()
for _ in range(t):
    n = int(input())
    s = [a for a in input()]
    s.sort()
    def run():
        if n != 5:
            return "NO"
        if s != name:
            return "NO"
        return "YES"
    print(run())