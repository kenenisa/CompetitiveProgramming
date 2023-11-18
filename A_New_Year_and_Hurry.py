from sys import stdin
input = stdin.readline
n,k=list(map(int,input().split()))
minutes = 4 * 60
minutes = minutes - k
mx = 0
for i in range(1,n+1):
    if mx + 5*i > minutes:
        print(i-1) 
        break
    elif mx + 5*i == minutes:
        print(i)
        break
    if i == n:
        print(n)
    mx += 5*i
