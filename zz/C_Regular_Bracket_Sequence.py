sq = input()
stack = []
result = 0
for s in sq:
    if s == "(":
        stack.append(s)
    else:
        if stack:
            result += 1
            stack.pop()
print(result*2)