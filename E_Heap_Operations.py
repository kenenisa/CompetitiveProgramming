from heapq import heappush, heappop

h  = []
cases = input()
results = []
for line in range(int(cases)):
    inp = input()
    inps = inp.split()
    if inps[0] == 'insert':
        heappush(h, int(inps[1]))
        results.append(inp)
    if inps[0] == 'removeMin':
        if h:
            heappop(h)
            results.append(inp)
        else:
            heappush(h, 99999)
            results.append('insert {}'.format(99999))
            heappop(h)
            results.append('removeMin')
    if inps[0] == 'getMin':
        while h and int(inps[1]) > h[0]:
            heappop(h)
            results.append('removeMin')
        if h and int(inps[1]) == h[0]:
            results.append('getMin {}'.format(h[0]))
        else:
            heappush(h, int(inps[1]))
            results.append('insert {}'.format(inps[1]))
            results.append('getMin {}'.format(h[0]))
print(len(results))
for r in results:
    print(r)