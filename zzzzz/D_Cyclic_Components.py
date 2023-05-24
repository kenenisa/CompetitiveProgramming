from collections import defaultdict
import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n,m=list(map(int,input().split()))
    df = defaultdict(list)
    edges = [0]*(n+1)
    visited = set()
    for _ in range(m):
        u,v=list(map(int,input().split()))
        df[u].append(v)    
        df[v].append(u)
        edges[u] += 1
        edges[v] += 1
    col = []
    def dfs(i):
        stack = [i]
        while stack:
            item = stack.pop()
            col.append(item)
            visited.add(item)
            for j in df[item]:
                if j not in visited:
                    stack.append(j)



    result = 0
    for i in range(1, n+1):
        if i not in visited:
            col.clear()
            dfs(i)
            valid = True
            for a in col:
                if edges[a] != 2:
                    valid = False
                    break
            if valid:
                result += 1
    print(result)

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()