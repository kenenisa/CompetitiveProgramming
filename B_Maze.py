from collections import deque
n, m, k = list(map(int, input().split()))


maze = []
visited = set()
s = -k
directions = [(1, 0), (0, 1), (0, 0), (-1, 0), (0, -1)]
c = 0
for i in range(n):
    maze.append(input())
    s += maze[-1].count('.')
for i in range(n):
    for j in range(m):
        if maze[i][j] == '.':
            startX = i
            startY = j
            break
q = deque()
q.append((startX, startY))
while q:
    v, u = q.popleft()
    for i, j in directions:
        if c >= s: break
        x = v-i
        y = u-j
        if x >= 0 and y >= 0 and x < n and y < m:
            if maze[x][y] == '.' and (x, y) not in visited:
                visited.add((x, y))
                q.append((x, y))
                c += 1

for i in range(n):
    result = []
    for j in range(m):
        if (i, j) in visited:
            result.append('.')
        else:
            if maze[i][j] == '.':
                result.append('X')
            else:
                result.append('#')

    print("".join(result))
