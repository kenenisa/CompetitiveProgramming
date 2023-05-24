from collections import defaultdict,deque

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    # write your code here


    n,m=list(map(int,input().split()))
    df = defaultdict(list)

    edges = []

    for _ in range(m):
        u,v=list(map(int,input().split()))
        df[u].append(v)
        df[v].append(u)
        edges.append(u)

    color = [0 for _ in range(n+1)]
    color[1] = 1
    def dfs(i):
        for j in df[i]:
            if color[i] == color[j]: return False
            if color[j] == 0:
                color[j] = 1 if color[i] == 2 else 2
                if not dfs(j):
                    return False
        return True

    color = [0 for _ in range(n+1)]
    color[1] = 1
    def dfs(item):
        queue = deque([item])
        while queue:
            i = queue.popleft()
            for j in df[i]:
                if color[i] == color[j]: return False
                if color[j] == 0:
                    color[j] = 1 if color[i] == 2 else 2 
                    queue.append(j)
        return True


    if dfs(1):
        print("YES")
        result = ["0"] * m
        for i in range(m):
            if color[edges[i]] == 1:
                result[i] = "1"
        print("".join(result))
    else:
        print("NO")

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()


