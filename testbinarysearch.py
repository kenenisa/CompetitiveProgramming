n = 100
p = 50
k = 1
# mid = 4
# m = p-mid+1
# s = (m/2) * ((2*p) + (m-1) * -1)
# print(s)
left = 1
right = p
s=0
while left < right:
    mid = (right+left)//2
    m = p-mid+1
    s = (m/2) * ((2*p) + (m-1) * -1)
    print(mid,m,s)
    if s == n:
        print('found it k=', mid)
    elif s > n:
        left = mid+1
    else:
        right = mid-1
print(left,right,s)
