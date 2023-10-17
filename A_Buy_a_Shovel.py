n, m = list(map(int, input().split()))

i = 1
while True:
    k = n*i
    if k % 10 == 0 or k % 10 == m:
        print(i)
        break
    i += 1
