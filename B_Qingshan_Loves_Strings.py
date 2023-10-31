

def checkIfGood(st):
    for i in range(len(st)-1):
        if st[i] == st[i+1]:
            return False
    return True
def run():
    n,m=list(map(int,input().split()))
    s = input()
    t = input()
    if n == 1 or checkIfGood(s):
        return "Yes"
    if not checkIfGood(t):
        return "No"
    if t[0] != t[-1]:
        return "No"
    one = s.count("11")
    zero = s.count("00")
    if one > 0 and zero > 0:
        return "No"
    if (one > 0 and t[0] == '0') or (zero > 0 and t[0] == '1'):
        return "Yes"
    return "No"

    

t = int(input())
for _ in range(t):
    print(run())