t = int(input())
for _ in range(t):
    n = int(input())
    bi = [a for a in input()]
    fh = n//2
    sh = n//2
    if n%2!=0:
        sh +=1
    first = bi[:fh]
    second = list(reversed(bi[sh:]))
    def run():
        diff = False
        sim = False
        for i in range(fh):
            if first[i] != second[i]:
                if diff and sim:
                    return "No"
                diff = True
            else:
                if diff:
                    sim =True
        return "Yes"
    print(run())