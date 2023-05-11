# from math import gcd
# from functools import reduce

# def factors(n):    
#     return set(reduce(list.__add__, 
#                 ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int,input().split()))
#     a.sort()
#     def run():
#         if gcd(*a) > n:
#             return "No"
#         for i in range(2,n+1):
#             # print( gcd(*a[:i]),i,a[:i])
#             if gcd(*a[:i]) > i:
#                 return "No"
#         return "Yes"
#     print(run())

# # print("======")
# # print(gcd(*[227821,143,4171,1941]))
import math
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    ans="NO"
    for i in range(n):
        for j in range(i+1,n):
            if math.gcd(l[i],l[j])<=2:ans="YES"
    print(ans)