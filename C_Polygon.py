
def run():
    n = int(input())
    mat = []
    for _ in range(n):
        mat.append(input())
    if n == 1: return "YES"
    for i in range(n-1):
        for j in range(n-1):
            if mat[i][j] == '1' and mat[i+1][j] == '0' and mat[i][j+1] == '0':
                return "NO"
    return "YES"
t = int(input())
for _ in range(t):
    print(run())