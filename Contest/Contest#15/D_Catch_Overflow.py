l = int(input())

stack = [1]
result = 0
limit = 1 << 32
for _ in range(l):
    s = input()
    if "for" in s:
        val = stack[-1] * int(s.split()[1])
        if limit > val:
            stack.append(val)
        else:
            stack.append(limit+1)

            
    elif "add" == s:
       result += stack[-1]
    else:
       stack.pop()
        
# valid = True
# for s in stack:
#     result += s[1]

if result >= limit:
    print("OVERFLOW!!!")
else:
    print(result)