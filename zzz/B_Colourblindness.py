t = int(input())
for _ in range(t):
    n = int(input())
    row1 = input()
    row2 = input()
    def run():
        for i in range(n):
            if row1[i] != row2[i] and  not ((row1[i] == 'G' and row2[i] == 'B') or (row1[i] == 'B' and row2[i] == 'G')):
                return "NO"
        return "YES"
    print(run())
        