n = int(input())
f = list(input())
s = list(input())
result = []
for i in range(n):
    if f[i]!= s[i]:
        result.append((f[i],s[i]))
        x = f[i]
        y = s[i]
        for j in range(n):
            if f[j] == x: f[j] = y
            if s[j] == x: s[j] = y
print(len(result))
for x,y in result:
    print(x,y)                    

