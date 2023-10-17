n = int(input())
result = [1] * (n+2)

used = False
for i in range(2,n+2):
    if result[i] == 1:
        for j in range(i*i,n+2,i):
            result[j] = 2
            used = True
k = 1
if used:
    k+=1
print(k)
print(*result[2:])