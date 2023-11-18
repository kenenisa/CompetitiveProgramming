n = int(input())
coin = [1, 5, 10, 20, 100]
coin.reverse()
count = 0
for c in coin:
    count += n//c
    n = n%c
print(count)