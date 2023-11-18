
t = int(input())
for tk in range(t):
    n = int(input())
    s = input()    
    def scenario(x,y):
        XA = XB = YA = YB =  0
        for i in range(len(s)):
            if YA == y or YB == y:
                return None
            if s[i] == 'A':
                XA += 1
            else:
                XB += 1
            if XA == x:
                YA += 1
                XA = XB = 0
            elif XB == x:
                YB += 1
                XA = XB = 0
        if YB < YA and YA == y:
            return 'A'
        elif YA < YB and YB == y:
            return 'B'
        return None
                
    resultA = 0
    resultB = 0
    for y in range(1,21):
        for x in range(1,21):
            sn = scenario(x,y)
            # if sn:
            #     print(tk,x,y,sn)
            if sn == 'A':
                resultA += 1
            elif sn == 'B':
                resultB += 1

    if (resultA > 0 and resultB > 0) or (resultA == resultB == 0):
        print('?')
    else:
        print('A' if resultA > 0 else 'B')


# AAAAAAAABBBAABBBBBAB