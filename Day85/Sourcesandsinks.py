t = int(input())
so = [False] * t
si = [False] * t
for i in range(t):
    a = list(map(int,input().split()))
    for j in range(t):
        if a[j] == 1:
            so[i] = True
            si[j] = True

sources = []
sinks = []
for i in range(t):
    if so[i] and not si[i]:
        sources.append(i+1)
    elif not so[i] and si[i]:
        sinks.append(i+1)
    elif not so[i] and not si[i]:
        sources.append(i+1)
        sinks.append(i+1)
sources.sort()
sinks.sort()
print(len(sources),*sources)
print(len(sinks),*sinks)



    