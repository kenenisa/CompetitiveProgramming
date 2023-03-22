t = int(input())
for _ in range(t):
    n = int(input())
    s = [a for a in input()]
    ops = {"0":"1","1":"0"}
    def run():
        i = 0
        while i < n:
            # print(s,i)
            while i < n and s[i] in ["1","0"]:
                i += 1
            if i == n:
                break
            p = i
            val = "1"
            l = s[i]
            if p > 0:
                val = ops[s[p-1]]
            while p < n:
                if l == s[p]:
                    if p > 0 and p < n - 1:
                        if (s[p-1] == "0" and  s[p+1] == "1") or (s[p-1] == "1" and s[p+1] == "0"):
                            return "NO"
                    s[p] = val
                p += 1
            i += 1
        for i in range(1,n):
            if s[i-1] == s[i]:
                return "NO"
        return "YES"
    print(run())


