import heapq
n = int(input())
w = list(map(int,input().split()))
s = input()

min_h = []
max_h = []
for i in range(n):
    heapq.heappush(min_h,[w[i],i+1])
result = []
for i in range(len(s)):
    if s[i] == "0":
        mi = heapq.heappop(min_h)
        mi[0] *= -1
        heapq.heappush(max_h,mi)
    else:
        mi = heapq.heappop(max_h)
    result.append(mi[1])
print(*result)




