class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int: 
        n = len(board)
        jump = defaultdict(int)
        flag = True
        count = 1
        for i in range(n-1,-1,-1):
            for j in (range(n) if flag else range(n-1,-1,-1)):
                if board[i][j] != -1:
                    jump[count] = board[i][j] 
                count += 1
            flag = not flag
        q = deque([(1,0)])
        visited = set()
        while q:
            square,d = q.popleft()
            for i in range(1,7): 
                j = square + i 
                if jump[j] > 0: 
                    j = jump[j]
                if j == n*n: 
                    return d+1
                if j not in visited: 
                    visited.add(j) 
                    q.append((j,d+1))
        return -1

