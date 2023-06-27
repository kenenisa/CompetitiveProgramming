n,m,k=list(map(int,input().split()))
players = []
for _ in range(m+1):
    players.append(int(input()))
fedor = players[-1]
result = 0
for i in range(m):
    r = bin(fedor ^ players[i])[2:].count("1")
    if r <= k:
        result += 1
print(result)

