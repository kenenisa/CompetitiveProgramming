n,m=list(map(int,input().split()))

def recur(val,move,count):
    if val == m:
        return count
    val *= move
    if val > m:
        return -1
    return max(recur(val,2,count+1),recur(val,3,count+1))
if n == m:
    print(0)
else:
    print(max(recur(n,2,0),recur(n,3,0)))