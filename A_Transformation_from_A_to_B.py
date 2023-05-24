n,m=list(map(int,input().split()))
sol = [m]
while n < m:
    if m % 2 == 1:
        if m % 10 != 1:
            break
        else:
            m = m//10 
    else:
        m = m//2
    sol.append(m)

if n == m:
    sol.reverse()
    print("YES")
    print(len(sol))
    print(*sol)
else:
    print("NO")