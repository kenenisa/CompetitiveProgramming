x = y = 0
for i in range(5):
    a = list(map(int, input().split()))
    found = False
    for j in range(5):
        if a[j] == 1:
            x = i
            y = j
    if found:
        break
print(abs(x-2) + abs(y-2))
