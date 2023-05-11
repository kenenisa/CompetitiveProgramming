n = input()
def recur(s):
    if len(s) == 1:
        return 0
    num = 0
    for a in s:
        num += int(a)
    return 1 + recur(str(num))
print(recur(n))
    
        