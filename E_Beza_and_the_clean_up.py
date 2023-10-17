import heapq

def max_value(n, m, s, A, B, a, b):
    a.sort(reverse=True)
    b.sort(reverse=True)
    pq = []
    ans = [0]*(s+1)
    j = 0
    
    for i in range(min(s//A, n)+1):
        while j < min(i, m) and A*(i-j-1) + B*(j+1) <= s:
            heapq.heappush(pq, b[j])
            j += 1
        if i > 0:
            heapq.heappush(pq, a[i-1])
        while len(pq) > 0 and A*(i-j) + B*j > s:
            heapq.heappop(pq)
        if len(pq) > 0:
            ans[A*(i-j) + B*j] = max(ans[A*(i-j) + B*j], sum(pq))
    
    return max(ans)

n, m, s, A, B = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(max_value(n, m, s, A, B, a, b))
