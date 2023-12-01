t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    if n == 1:
        print(a[0]-1)
        continue
    com = [1]
    for i in range(n):
        if a[i] != com[-1]:
            com.append(a[i])
    result = 0
    for i in range(len(com)-1):
        if com[i] < com[i+1]:
            result += com[i+1] - com[i]
    print(result)

