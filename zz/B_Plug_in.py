st = input()
stack = []

for s in st:
    if stack and stack[-1] == s:
        stack.pop()
    else:
        stack.append(s)
print("".join(stack))