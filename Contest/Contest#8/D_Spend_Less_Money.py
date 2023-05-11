n,k=list(map(int,input().split()))
now = list(map(int,input().split()))
later = list(map(int,input().split()))
items = []

for i in range(n):
    items.append((now[i],later[i],now[i]-later[i]))
items.sort(key=lambda item:item[2])

buyNow = 0
buyLater = 0
for i in range(n):
    if k > 0:
        buyNow += items[i][0]
        k-=1
    else:
        if items[i][2] < 0:
            buyNow += items[i][0]
        else:
            buyLater += items[i][1]
print(buyNow + buyLater)