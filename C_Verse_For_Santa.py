
t = int(input())
for _ in range(t):
    n,s=list(map(int,input().split()))
    a = list(map(int,input().split()))
    c = 0
    valid = False 
    i = 0
    while i < n:
        c += a[i]
        if c > s:
            valid = True
            break  
        i+=1
    i+=1
    if not valid:
        print(0)
        continue
    mx = max(a[:i])
    for i in range(n):
        if a[i] == mx:
            print(i+1)
            break
	    

	     