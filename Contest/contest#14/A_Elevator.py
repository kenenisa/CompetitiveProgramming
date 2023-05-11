t = int(input())
for _ in range(t):
    wt,et,ef=list(map(int,input().split()))

    walk = wt * 4
    walk_to_elev = wt * ef + ((4 - ef) * et)
    take_elev = ef * et + et * 4
    print(min(walk,walk_to_elev,take_elev))