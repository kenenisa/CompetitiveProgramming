n,l,r=list(map(int,input().split()))
# result = 0
# # memo = {}
# def recur(x):
#     # if x in memo:
#     #     return memo[x]
#     if x <= 1:
#         return [x]
#     # memo[x] = 
#     return recur(x//2) + [x%2] + recur(x//2)
# ls = recur(n)
# for i in range(l-1,r):
#     result += ls[i]
# print(result) 


exp = 1
result = 0
def recur(start,end,l,r,x):
    global result
    if start > end or l > r:
        return
    else:
        middle = (start + end) // 2
        if r < middle:
            recur(start, middle - 1, l, r, x // 2)
        elif middle < l:
            recur(middle + 1, end, l, r, x // 2)
        else:
            result += x % 2
            recur(start, middle - 1, l, middle - 1, x // 2)
            recur(middle + 1, end, middle + 1, r, x // 2)
cont = n
while cont >= 2:
    exp = exp * 2 + 1
    cont /= 2
# print(s)

recur(1, exp, l, r, n)
print(result)

