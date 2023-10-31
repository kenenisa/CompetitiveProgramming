def check(s):
    n = len(s)
    for i in range(n):
        if s[i] == s[n-i-1]:
            return False
    return True
def replacer(s):
    n = len(s)
    for i in range(n):
        if s[i] == s[n-i-1]:
            x = n-i-1
            if s[i] == "0":
                x = n-i
            s = s[:x] + '01' + s[x:]
            return (x,s)
def run():
    n = int(input())
    s = input()
    if check(s):
        print(0)
        return ""
    p = []
    count = 0
    while not check(s) and count < 300:
        x,t = replacer(s)
        p.append(x)
        s = t
        count += 1
    if count >=300 or not check(s):
        return -1
    print(len(p))
    return " ".join(map(str,p))

# 001110
# 001110
# 01001110

# 010110
# 0101100101
# 0011100011
t = int(input())
for _ in range(t):
    print(run())