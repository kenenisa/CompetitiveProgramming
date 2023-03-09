n = int(input())
a = list(map(int,input().split()))

pos = 0
zero = 0
neg = 0

coins = 0
for i in range(n):
    if a[i] < 0:
        neg += 1
        coins += -1 - a[i]
    elif a[i] > 0:
        pos += 1
        coins += a[i] - 1
    else:
        zero += 1
if zero > 0:
    coins += zero
if neg%2==1:
    if zero == 0:
        coins += 2
print(coins)