s,n= list(map(int,input().split()))
dragons = []
for _ in range(n):
    dragons.append(list(map(int,input().split())))
def srt(k):
    return k[0]
dragons.sort(key=srt)
def isPos(s):
    for drag in dragons:
        if s > drag[0]:
            s += drag[1]
        else:
            return "NO"
    return "YES"
print(isPos(s))