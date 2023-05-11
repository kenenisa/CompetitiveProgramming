test = int(input())
 
for _ in range(test):
    n = int(input())
    el = len(set(input().split()))
    result = [str(max(i+1,el)) for i in range(n)]
    print(" ".join(result))
