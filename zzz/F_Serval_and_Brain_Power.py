def is_powerful(s):
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0 and s[:i] * (n // i) == s:
            return True
    return False

def find_subsequences(s):
    n = len(s)
    mx = 0
    for i in range(1, 2**n):
        sub = ""
        for j in range(n):
            if (i >> j) & 1:
                sub += s[j]
        if len(sub) > 1:
            if is_powerful(sub):
                mx = max(mx,len(sub))
    return mx
print(find_subsequences(input()))







