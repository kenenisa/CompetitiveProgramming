def check(arr):
    # print(arr)
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return True
    return False
def run():
    n = int(input())
    a = list(map(int,input().split()))
    if n < 3: return "YES"
    if not check(a): return "YES"
    for m in range(2,6):
        if check(a[2**(m-1):(2**m)]):
            return "NO"
    return "YES"

t = int(input())
for i in range(t):
    # print(i+1)
    print(run())
    