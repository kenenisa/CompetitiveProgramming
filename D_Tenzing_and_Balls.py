from collections import defaultdict, deque


"""
####
#### I KNOWWWW IT'S TLE AT BEST
### IF NOT MOST PROBABLY WRONG
### DON'T SUBMIT THISS
### SECOND SUBMISSION IK IT'S TLE SIMON IDK WHAT TO DO
"""
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    def dp():
        removed = [0] * n
        while True:
            start = defaultdict(lambda: -1)
            end = defaultdict(lambda: -1)
            visited = set()
            valid = False
            for i in range(n):
                if removed[i] == 0:
                    if a[i] in visited:
                        valid = True
                        end[a[i]] = i
                    else:
                        start[a[i]] = i
                        visited.add(a[i])
            if not valid:
                return removed.count(0)
            m = []
            for v in visited:
                if v in start and v in end:
                    m.append((end[v]-start[v], v))
            m.sort(reverse=True)
            v = m[0][1]
            # result.append(dp(arr[:start[v]] + arr[end[v]+1:]))
            for i in range(start[v], end[v]+1):
                removed[i] = 1
    print(n - dp())
