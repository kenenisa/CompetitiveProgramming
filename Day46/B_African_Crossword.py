n,m = list(map(int,input().split()))
grid = []
for _ in range(n):
    grid.append([[a,'.'] for a in input()])
# rows
for i in range(n):
    df = {}
    for j in range(m):
        if grid[i][j][0] in df:
            grid[i][df[grid[i][j][0]]][1] = 'x'
            grid[i][j][1] = '#'
        df[grid[i][j][0]] = j
        
for j in range(m):
    df = {}
    for i in range(n):
        if grid[i][j][0] in df:
            grid[df[grid[i][j][0]]][j][1] = 'x'
            grid[i][j][1] = '#'
        df[grid[i][j][0]] = i
word = []
for i in range(n):
    for j in range(m):
        if grid[i][j][1] == '.':
            word.append(grid[i][j][0])
print("".join(word))

