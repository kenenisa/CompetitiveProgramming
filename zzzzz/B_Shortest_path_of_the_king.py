import math
def dist(st):
    return (ord(st[0])-96,int(st[1]))
s = dist(input())
t = dist(input())

directions = [(-1,0),(1,0),(0,1),(0,-1),(-1,1),(-1,-1),(1,1),(1,-1)]
anot = [ "L", "R", "U", "D", "LU", "LD", "RU", "RD"]

def distance(x1,x2,y1,y2):
    return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))

def direct(x,y,i,j):
    x = x+i
    y = y+j
    if 1 <= x <= 8 and 1 <= y <= 8:
        return (x,y)
    return False
di = distance(s[0],t[0],s[1],t[1])
result = []

while not (s[0] == t[0] and s[1] == t[1]):
    mi = 0
    nd = False
    for i in range(8):
        a,b = directions[i]
        new_dir = direct(s[0],s[1],a,b)
        if new_dir:
            c,d = new_dir
            new_d = distance(c,t[0],d,t[1])
            if new_d < di:
                di = new_d
                mi = i
                nd = new_dir
    if nd:
        s = nd
    result.append(anot[mi])
print(len(result))
for r in result:
    print(r)
    


