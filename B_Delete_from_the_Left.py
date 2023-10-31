s = input()
t = input()
n = len(s)
m = len(t)
i = 0
while i < n and i < m and s[n-i-1] == t[m-i-1]:
    i+=1
print((n+m)-(i*2))