t = int(input())

for _ in range(t):
    board = []
    input()
    for _ in range(8):
        board.append([s for s in input()])
    def findTheBishop():
        for i in range(1,7):
            for j in range(1,7):
                if board[i][j] == '#':
                    if board[i-1][j-1] == '#' and board[i+1][j-1] == '#' and board[i+1][j+1] == '#' and board[i-1][j+1] == '#':
                        return [i,j]
    f = findTheBishop()
    print(f[0]+1,f[1]+1)
        
                        