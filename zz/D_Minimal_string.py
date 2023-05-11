s = input()
n = len(s)
l = [0] * 26

for i in range(n):
    l[ord(s[i]) - 97] += 1
def check(letter):
    for i in range(ord(letter)-97):
        if l[i] > 0:
            return False
    return True
t = []
u = []
for i in range(n):
    t.append(s[i])
    l[ord(s[i]) - 97] -= 1
    while t and check(t[-1]):
        u.append(t.pop())
print("".join(u))
