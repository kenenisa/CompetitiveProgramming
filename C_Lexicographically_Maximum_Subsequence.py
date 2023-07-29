from collections import defaultdict
s = input()
df = {}
for i in range(len(s)):
    df[s[i]] = i
l = sorted(df.items())
result = []

n = len(s)
i = 0
while i < n:
    item,pos = l.pop()
    while i <= pos:
        if s[i] == item:
            result.append(item)
        i+=1
    # i+=1
print(''.join(result))