a = list(set(map(int,input().split(","))))
a.sort()
n = len(a)
result = [[a[0]]]

for i in range(1,n):
    if a[i] - a[i-1] == 1:
        if len(result[-1]) == 1:
            result[-1].append(a[i])
        else:
            result[-1][1] = a[i]
    else:
        result.append([a[i]])
def addDash(item):
    return "-".join(map(str,item))
print(",".join(list(map(addDash,result))))
