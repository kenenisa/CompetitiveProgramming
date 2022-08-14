#q4
cases = input()
for line in range(int(cases)):
    s = input()
    n = len(s)
    m = 3
    if n < m: 
        print(0)
        continue
    pat = [0] * 256
    st = [0] * 256
    for i in range(0, m): pat[ord("123"[i])] += 1
    start = 0
    si = -1 
    ml = float('inf')
    c = 0 
    for j in range(0, n):
        st[ord(s[j])] += 1
        if (st[ord(s[j])] <=
                pat[ord(s[j])]):
            c += 1
        if c == m:
            while pat[ord(s[start])] == 0 or st[ord(s[start])] > pat[ord(s[start])]:
                if (st[ord(s[start])] >
                        pat[ord(s[start])]):
                    st[ord(s[start])] -= 1
                start += 1
            lw = j - start + 1
            if ml > lw:
                ml = lw
                si = start
    if si == -1:
        print(0)
        continue
    print(len(s[si: si + ml]))



#q3
# n,t = map(int,input().split(" "))
# a = list(map(int,input().split(' ')))
# cells = list(range(1,n+1))
# i = 0
# while i < n and cells[i] < t:
#     i += a[i]
# print("YES" if i < n and cells[i] == t else "NO")




#q2
# n,m = input().split(" ")
# a = input().split(' ')
# b = input().split(' ')
# prefix = [0,int(a[0])]
# for i in range(1,int(n)):
#     prefix.append(prefix[-1] + int(a[i]))
# def binarySearch(bi, start,end):
#     if start == end:
#         return start
#     mid = (start+end)//2
#     if prefix[mid] >= bi:
#         return binarySearch(bi,start,mid)
#     return binarySearch(bi,mid+1,end)
# for bi in b:
#     p = binarySearch(int(bi),0,int(n))
#     print(p, int(bi) - prefix[p - 1])




#q1
# fault = -1
# cases = input()
# def checkBrackets(s,n):
#     global fault
#     stack = []
#     for i in range(n):
#         if s[i] == '(':
#             stack.append(s[i])
#         elif s[i] == ')':
#             if not stack:
#                 fault = i
#                 return False
#             stack.pop()
#     return True
# for line in range(int(cases)):
#     n = int(input())
#     s = list(input())
#     count = 0
#     while not checkBrackets(s,n):
#         count += 1
#         b = s.pop(fault)
#         if b == '(':
#             s.insert(0,'(')
#         else:
#             s.append(')')
#     print(count)