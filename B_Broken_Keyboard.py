t = int(input())
for _ in range(t):
    s = input()
    result = []
    for i in set(s):
        c = s.count(i+i)
        if s.count(i) > 2*c:
            result.append(i)
    result.sort()
    print("".join(result))
