t = int(input())

for i in range(t):
    a,y,z=list(map(int,input().split()))
    if (y - (z - y) >= a and (y - (z - y)) % a == 0 and y - (z - y) != 0) or (a + (z - a)/2 >= y and (z-a)%2 == 0 and (a + (z - a)/2) % y == 0 and a + (z - a)/2 != 0) or a + 2*(y - a) >= z and (a + 2*(y - a)) % z == 0 and a + 2*(y - a) != 0:
        print("YES")
    else:
        print("NO")
