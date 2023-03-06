n,m,k=list(map(int,input().split()))
room = []
for _ in range(n):
    room.append([a for a in input()])


ways = 0
# find rows
for i in range(n):
    seat = 0
    for j in range(m):
        if room[i][j] == '.':
            seat += 1
        else:
            if seat >= k:
                ways += seat - k + 1
            seat = 0
    if seat >= k:
        ways += seat - k + 1  
# find cols
for j in range(m):
    seat = 0
    for i in range(n):
        if room[i][j] == '.':
            seat += 1
        else:
            if seat >= k:
                ways += seat - k + 1
            seat = 0
    if seat >= k:
        ways += seat - k + 1
if k == 1:
    ways = int(ways / 2)
print(ways)

