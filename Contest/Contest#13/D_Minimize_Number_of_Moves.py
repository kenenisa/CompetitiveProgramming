t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    def recur(pat,l):
        m = len(pat)
        if m == 1:
            if l == pat[0]:
                return 0
            return 1
        fh = pat[:m//2]
        sh = pat[m//2:]
        fhc = fh.count(l)
        shc = sh.count(l)
        return min(((m//2) - shc) + recur(fh,chr(ord(l) + 1)), ((m//2) - fhc) + recur(sh,chr(ord(l) + 1)))
    print(recur(s,'a'))
        

