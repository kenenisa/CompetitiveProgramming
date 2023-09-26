
n = int(input())
a = list(map(int,input().split()))

yestr = 0
rest = 0
for i in range(n):
    if a[i] == 0:
        yestr = 0
        rest += 1
    elif a[i] == yestr:
        yestr = 0
        rest += 1
    elif a[i] == 1:
        yestr = a[i]
    elif a[i] == 2:
        yestr = a[i]
    else:
        if yestr > 0:
            yestr = 3 - yestr
print(rest)
                
	