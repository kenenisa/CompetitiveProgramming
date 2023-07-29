from collections import *
def run():
    n = int(input())
    r1,c1 = list(map(int,input().split()))
    r2,c2 = list(map(int,input().split()))
    square = []
    for _ in range(n): square.append(input())

    directions = [(1,0),(-1,0),(0,-1),(0,1)]
    def bfs(i,j):
        r = []
        q = deque([(i,j)])
        visited = set([(i,j)])

        while q:
            item = q.popleft()
            r.append(item)
            for dx,dy in directions:
                x = item[0] + dx 
                y = item[1] + dy
                if 0 <= x < n and 0 <= y < n and (x,y) not in visited and square[x][y] == '0':
                    q.append((x,y))
                    visited.add((x,y))
        return r
    start = bfs(r1-1,c1-1)
    end = bfs(r2-1,c2-1)

    if set(start) & set(end):
        return 0
    result = float('inf')
    for a,b in start:
        for c,d in end:
            result = min(result,(a-c)**2+(b-d)**2)
    return result
print(run())





    


