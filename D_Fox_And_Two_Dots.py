n, m = map(int, input().split())
df = []
for _ in range(n):
    df.append(input())

directions = [(0, 1), (0, -1), (-1, 0),(1, 0)]
def dfs(x, y, px, py, visited):
    visited.add((x, y))
    for dx, dy in directions:
        i = x+dx
        j = y+dy
        if (i == px and j == py) or i < 0 or i >= n or j < 0 or j >= m or df[i][j] != df[x][y]:
            continue
        if (i, j) in visited or dfs(i, j, x, y, visited):
            return True
    return False

def run():
    for i in range(n):
        for j in range(m):
            if dfs(i, j, -1, -1, set()):
                return "Yes"
    return "No"
print(run())
