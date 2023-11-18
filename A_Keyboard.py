from collections import defaultdict, deque

keyboard = 'qwertyuiopasdfghjkl;zxcvbnm,./'

df = defaultdict(int)
for a in range(len(keyboard)):
    df[keyboard[a]] = a

s = input()
im = input()

r = ""
for i in im:
    if s == "R":
        r += keyboard[df[i]-1]
    else:
        r += keyboard[df[i]+1]
print(r)
