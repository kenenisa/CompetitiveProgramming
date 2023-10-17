# t = int(input())
# for _ in range(t):
#     n = int(input())

#     a = list(map(int, input().split()))
#     prefix = []
#     bits = [[0, 0] for _ in range(32)]
#     prefix.append(bits[::])
#     for i in range(n):
#         for k in range(32):
#             if a[i] & (1 << k):
#                 bits[k][1] += 1
#             else:
#                 bits[k][0] += 1
#         prefix.append(bits[::])
#     q = int(input())
#     def getPrefixSum(i, j):
#         setBits = 0
#         for k in range(32):
#             left = prefix[i][k]
#             right = prefix[j][k]
#             if right[0] - left[0] < 1 and right[1] - left[1] > 0:
#                 setBits = ((1 << k) | setBits)
#         print(i,j,setBits)
#         return setBits
#     ans = []
#     for _ in range(q):
#         l, k = list(map(int, input().split()))
#         l-=1
#         left = l
#         right = n-1
#         result = -2
#         while left < right:
#             mid = (right + left) // 2
#             if getPrefixSum(l,mid) >= k :
#                 result = mid
#                 left = mid +1
#             else:
#                 right = mid-1
#         ans.append(result+1)
#     print(*ans)
import sys
# readline
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    prefix = [[-1]*n for _ in range(32)]
    for i in range(32):
        prefix[i][0] = (1 & (a[0] >> i))
        for l in range(1, n):
            prefix[i][l] = prefix[i][l-1] + ((a[l] >> i) & 1)
    q = int(input())
    result = []
    for p in range(q):
        l, k = map(int, input().split())
        l -= 1
        left = l
        right = n-1
        r = -1
        while left <= right:
            mid = (left+right)//2
            val = 0
            for j in range(32):
                if l == 0:
                    prefixSum = prefix[j][mid]
                else:
                    prefixSum = prefix[j][mid]-prefix[j][l-1]
                if prefixSum == mid-l+1:
                    val = val | (1 << j)
            if val < k:
                right = mid-1
            else:
                left = mid+1
                r = mid+1
        result.append(r)
    print(*result)
