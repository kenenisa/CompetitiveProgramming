from collections import deque
t = int(input())
for _ in range(t):
    def run():  
        n,m=list(map(int,input().split()))
        maze = []
        good = []
        bad = []

        for i in range(n):
            row = input()
            maze.append(list(row))
            for j in range(m):
                if row[j] == "G":
                    good.append((i,j))
                elif row[j] == "B":
                    bad.append((i,j))
        if len(good) == 0:
            return "Yes"
        if maze[n-2][m-2] == "B" or maze[n-2][m-1] == "B" or maze[n-1][m-2] == "B":
            return "No"
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        for i,j in bad:
            for dx,dy in directions:
                x = i + dx
                y = j + dy
                if 0 <= x < n and 0 <= y < m:
                    if maze[x][y] == "G":
                        return "No"
                    if maze[x][y] == '.':
                        maze[x][y] = "#"
        visited = set()
        q = deque([(n-1,m-1)])

        while q:
            ci,cj = q.popleft()
            for dx,dy in directions:
                x = ci + dx
                y = cj + dy
                if 0 <= x < n and 0 <= y < m:
                    if (x,y) not in visited and maze[x][y] != '#':
                        visited.add((x,y))
                        q.append((x,y))


        for x,y in good:
            if (x,y) not in visited:
                return "No"
        for x,y in bad:
            if (x,y) in visited:
                return "No"
        return "Yes"
    print(run())
                        



