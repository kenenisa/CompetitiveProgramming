from collections import defaultdict
t = int(input())
for _ in range(t):
    n= int(input())
    grid = []
    for _ in range(n):
        grid.append([int(a) for a in input()])
    operations = 0
    corners = [[0,0],[0,n-1],[n-1,n-1],[n-1,0]]
    for i in range(n//2):
        rot = [c[:] for c in corners]
        for j in range(n-1-(i*2)):
            # prepare corners
            count = defaultdict(int)
            count[grid[rot[0][0]][rot[0][1]]] += 1
            count[grid[rot[1][0]][rot[1][1]]] += 1
            count[grid[rot[2][0]][rot[2][1]]] += 1
            count[grid[rot[3][0]][rot[3][1]]] += 1
            operations += min(count[0],count[1])
            # next to be rotated
            rot[0][1] += 1
            rot[1][0] += 1
            rot[2][1] -= 1
            rot[3][0] -= 1
        # move the corners inside
        corners[0][0] += 1
        corners[0][1] += 1

        corners[1][0] += 1
        corners[1][1] -= 1
        
        corners[2][0] -= 1
        corners[2][1] -= 1
        
        corners[3][0] -= 1
        corners[3][1] += 1
    print(operations)