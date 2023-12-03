from collections import defaultdict,deque

grid = [
    input(),
    input(),
    input(),
]
l = list(grid[0] + grid[1] + grid[2])
l.sort()
start = l[0]
directions = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1),
    (-1,-1),
    (1,1),
    (-1,1),
    (1,-1),
]
def bfs(i,j):
    formed = []
    q = deque([(grid[i][j],[(i,j)])])
    while q:
        node,path = q.popleft()
        # print(node,path)
        if len(node) == 3:
            formed.append(node)
        else:
            for dx,dy in directions:
                x = path[-1][0] + dx
                y = path[-1][1] + dy
                if 0 <= x < 3 and 0 <= y < 3 and (x,y) not in path:
                    q.append((node+grid[x][y],path+[(x,y)]))
    formed.sort()
    return formed[0]

found = []
for i in range(3):
    for j in range(3):
        if grid[i][j] == start:
            found.append(bfs(i,j))
found.sort()
print(found[0])
