t = int(input())
for _ in range(t):
    darts = []
    for i in range(10):
        s = input()
        for j in range(10):
            if s[j] == "X":
                darts.append([i, j])
    points = 0
    for x, y in darts:
        for i in range(5):
            if (x in (0+i,9-i) and y in range(0+i, (9-i)+1)) or (y in (0+i,9-i) and x in range(0+i, (9-i)+1)):
                points += (i+1)
                break
    print(points)
