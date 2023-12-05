import os

cd = os.getcwd()
with open('day05.txt', 'r') as file:
    count = 0
    lookingFor = []
    nxt = []
    inputString = ''
    last = 'seed'
    df = {}
    index = []
    for line in file:
        if line == '\n':
            continue
        elif line[:5] == 'seeds':
            nxt = list(map(int, line.split(':')[1].strip().split()))
        elif line[0] in '0987654321':
            df[last].append(list(map(int, line.split())))
        elif line and line[0] not in '0987654321':
            last = line.split()[0]
            df[last] = []
            index.append(last)
    lookingFor = []
    for i in range(0, len(nxt), 2):
        lookingFor += list(range(nxt[i], nxt[i]+nxt[i+1]))
    for ind in index:
        visited = set()
        transform = {}
        for d, s, r in df[ind]:
            for i in range(len(lookingFor)):
                l = lookingFor[i]
                diff = l-s
                if l >= s and diff < r:
                    transform[i] = d+diff
                    visited.add(i)
        nxt = []
        for i in range(len(lookingFor)):
            if i in visited:
                nxt.append(transform[i])
            else:
                nxt.append(lookingFor[i])
        lookingFor = nxt[:]
    print(min(lookingFor))