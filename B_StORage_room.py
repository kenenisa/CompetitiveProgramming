t = int(input())
for _ in range(t):
    n = int(input())
    table = []
    result = [0]*n
    if n == 1:
        input()
        print("YES")
        print(7)
        continue
    for j in range(n):
        a = list(map(int, input().split()))
        temp = a[0] if j != 0 else a[1]
        for i in range(n):
            if i != j:
                temp &= a[i]
        result[j] = temp
        table.append(a)
    valid = True
    # checker
    for i in range(n):
        if not valid:
            break
        for j in range(n):
            if i != j:
                if table[i][j] != (result[i] | result[j]):
                    valid = False
                    break
    if valid:
        print("YES")
        print(*result)
    else:
        print("NO")
