import random
t = int(input())
def suf(s):
    random.shuffle(s)
    if s == s[::-1]:
        return suf(s)
    return s
for _ in range(t):
    s = input()
    n = len(s)
    def the(s):
        if n == 1:
            return -1
        # check if it's palindrome
        if s != s[::-1]:
            return s
        else:
            # it is a pale
            if s == s[0] * n:
                return -1
            else:
                return "".join(suf([a for a in s]))
    print(the(s))