t = int(input())
for _ in range(t):
    n= int(input())
    grid = []
    for _ in range(n):
        grid.append([int(a) for a in input()])
    operations = 0
    for i in range(n):
        for j in range(n//2):
            if grid[i][j] != grid[i][n-j-1]:
                operations += 1
    for i in range(n//2):
        for j in range(n):
            if grid[i][j] != grid[n-i-1][j]:
                operations += 1
    print(operations)
1 1 1 0 0
1 1 0 1 1
0 1 0 1 1 
1 0 0 1 1
1 1 0 0 0