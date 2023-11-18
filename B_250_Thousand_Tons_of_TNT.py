# def run():
#     n = int(input())
#     a = list(map(int, input().split()))
#     if n == 1:
#         return 0
#     # a.sort()
#     result = 0

#     def calc(k):
#         weights = []
#         for i in range(0,n,k):
#             s = 0
#             for j in range(i,i+k):
#                 s += a[j]
#             weights.append(s)
#         return abs(max(weights)-min(weights))
#     for i in range(1, n):
#         if n % i == 0:
#             result = max(result, calc(i))
#     return result

# t = int(input())
# for _ in range(t):
#     print(run())

m= 0
for i in range(2,150000+1):
    d = 0
    for j in range(2,i):
        if i%j==0:
            d+=1
    m=max(m,d)
print(m)

