import string
ss = input()
n = len(ss)
l = 0
for s in ss:
    if s in string.ascii_lowercase:
        l += 1
if l < n - l:
    print(ss.upper())
else:
    print(ss.lower())