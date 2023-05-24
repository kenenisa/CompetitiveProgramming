from collections import defaultdict

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n,m=list(map(int,input().split()))
    a = list(map(int,input().split()))
    df = defaultdict(list)
    for _ in range(m):
        u,v=list(map(int,input().split()))
        df[u].append(v)
        df[v].append(u)
    visited = set()

    def dfs(i):
        if i in visited: return
        visited.add(i)
        for j in df[i]:
            dfs(j)
    a = [(a[i],i+1) for i in range(n)]
    a.sort(key=lambda item:item[0])

    result = 0
    for cost,i in a:
        if i not in visited:
            result += cost
            dfs(i)
    print(result)

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()