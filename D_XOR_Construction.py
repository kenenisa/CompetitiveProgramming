n = int(input()) 
a = list(map(int, input().split())) 
b = [0] * n 
b[0] = 0 
for i in range(1, n): 
    b[i] = b[i-1] ^ a[i-1] 
print(*b)


idd