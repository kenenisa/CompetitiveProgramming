n,m=list(map(int,input().split()))
flag = False
for i in range(n):
    if i % 2 == 0:
        print("#"*m)
    else:
        e = ["."] * m
        if flag:
            e[0] = "#"
        else:
            e[m-1] = "#"
        print("".join(e))
        flag = not flag



