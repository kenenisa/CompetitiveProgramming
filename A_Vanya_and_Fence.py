n,h=list(map(int,input().split()))
al = list(map(int,input().split()))
result = 0
for a in al:
    if a > h:
        result += 2
    else:
        result += 1

print(result)