lines = [
'3 5 2 10',
'6 7 6 10',
'6 7 4 10'
]

for x in range(0,len(lines)):
    line = list(map(int,lines[x].split()))
    pieces = line[:-1]
    l = line[-1]
    amount = 0
    while pieces:
        k = l
        j = 0
        while k>0 and j<len(pieces):
            if(pieces[j] <= k):
                val = pieces.pop(j)
                k = k - val
            else:
                j += 1 
        amount += 1
    print(amount)
        # print(max(a[:i]+a[i+1:]))



