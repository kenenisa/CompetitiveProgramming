a = list(input())
s = list(input())
s.sort()
result = []
for i in range(len(a)):
    if s and s[-1] > a[i]:
        result.append(s.pop())
    else:
        result.append(a[i])
print("".join(result))
