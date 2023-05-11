tests = int(input());

def customSort(item):
    return item[0]
for _ in range(tests):
    n,k = list(map(int,input().split()))
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    take = []
    for i in range(n):
        take.append([a[i],b[i]])
    take.sort(key=lambda x:x[0])

    for i in range(n):
        if(take[i][0] <= k):
                k += take[i][1]
        else:
            break

    print(k)
