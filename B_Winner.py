from collections import defaultdict

t = int(input())
df = {}
players = []
for i in range(t):
    name, score = input().split()
    score = int(score)
    if name in df:
        df[name] += score
    else:
        df[name] = score
    players.append((name, score))
m = max(df.values())
ds = {}
for name, score in players:
    if name in ds:
        ds[name] += score
    else:
        ds[name] = score
    if m <= ds[name] and df[name] == m:
        print(name)
        break
