t = int(input())
for _ in range(t):
    n,m = list(map(int,input().split()))
    board = []
    for i in range(n):
        board.append(list(map(int,input().split())))
    def bishop(i,j,n,m):
        s = board[i][j]
        # down right
        r = i + 1
        c = j + 1
        while r < n and c < m:
            s += board[r][c]
            r += 1
            c += 1
        # up right
        r = i - 1
        c = j + 1
        while r >= 0 and c < m:
            s += board[r][c]
            r -= 1
            c += 1
        # down left
        r = i + 1
        c = j - 1
        while c >= 0 and r < n:
            s += board[r][c]
            r += 1
            c -= 1
        # up left
        r = i - 1
        c = j - 1
        while c >= 0 and r >= 0:
            s += board[r][c]
            r -= 1
            c -= 1
        return s
    result = 0
    for i in range(n):
        for j in range(m):
            b = bishop(i,j,n,m)
            result = max(result,b)
    print(result)